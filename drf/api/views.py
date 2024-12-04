from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .task_generator import TaskGenerator


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leaderboard_view(request):
    users = User.objects.order_by('-mmr')[:25]
    serializer = UserSerializer(users, many=True)

    return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enemy_view(request):
    user = request.user
    try:
        room = Room.objects.filter(
            models.Q(first_user=user) | models.Q(second_user=user)
        ).first()
        enemy = room.first_user if room.first_user != user else room.second_user

        return JsonResponse(
            data={
                'result': 'race is going',
                'float': enemy.task_index / 10
            }, status=status.HTTP_200_OK
        )


    except Exception: # Room.DoesNotExist:
        return JsonResponse(
            data={
                'result': 'lose',
                'difference': 10
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def answer_view(request):
    try:
        answer = int(request.GET.get('answer'))
    except (ValueError, TypeError):
        return JsonResponse(
            {'error': 'answer must be an integer (or float)'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = request.user
    room = Room.objects.filter(
        models.Q(first_user=user) | models.Q(second_user=user)
    ).first()
    if not room:
        return Response(
            {'error': 'Room not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    enemy = room.first_user if room.first_user != user else room.second_user

    tasks = RoomTask.objects.filter(room=room).order_by('id')

    current_task = tasks[user.task_index]
    if current_task.answer == answer:
        user.task_index += 1
        user.save()

        if user.task_index == len(tasks):
            user.task_index = 0
            user.mmr += 10
            user.save()

            enemy.task_index = 0
            enemy.mmr -= 10
            enemy.save()

            room.delete()

            return JsonResponse(
                data={
                    'result': 'win',
                    'difference': 10
                },
                status=status.HTTP_200_OK
            )

        return JsonResponse(
            data={
                'result': 'good answer',
                'task': tasks[user.task_index].text,
                'float': user.task_index / 10
            },
            status=status.HTTP_200_OK, safe=False
        )

    return JsonResponse(
        data={'result': 'bad answer'},
        status=status.HTTP_200_OK
    )


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def room_view(request):
    if request.method == 'GET':
        return handle_room_get(request)
    return handle_room_delete(request)


def handle_room_get(request):
    user = request.user

    try:
        task_count = int(request.GET.get('task_count'))
        if not 5 <= task_count <= 20:
            raise ValueError
    except (TypeError, ValueError):
        return JsonResponse(
            {"error": "task_count must be an integer between 5 and 20"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        room = Room.objects.get(first_user=user)
        tasks = RoomTask.objects.filter(room=room).order_by('id')
        if not len(tasks):
            raise Exception
        current_task = tasks[user.task_index]

        if room.second_user:
            return JsonResponse({
                'result': 'joined',
                'other_user': UserSerializer(room.second_user).data,
                'task': current_task.text,
                'float': user.task_index / 10
            })
        return JsonResponse({'result': 'waiting'})

    except Exception:  # Room.DoesNotExist:
        return handle_room_creation(user, task_count)


def handle_room_creation(user, task_count):
    available_rooms = Room.objects.filter(second_user__isnull=True, task_count=task_count)

    if available_rooms.exists():
        room = available_rooms.first()
        room.second_user = user
        room.save()

        current_task = RoomTask.objects.filter(room=room).order_by('id')[user.task_index]
        return JsonResponse({
            'result': 'joined',
            'other_user': UserSerializer(room.first_user).data,
            'task': current_task.text,
            'float': user.task_index / 10
        })

    room = Room.objects.create(first_user=user, task_count=task_count)

    for i, (text, answer) in enumerate(TaskGenerator(task_count), 1):
        RoomTask.objects.create(room=room, text=text, answer=answer)

    return JsonResponse({'result': 'created'})


def handle_room_delete(request):
    user = request.user

    try:
        room = Room.objects.get(first_user=user)
    except Room.DoesNotExist:
        return JsonResponse(
            {'error': 'Room not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if room.second_user is None:
        room.delete()
        return JsonResponse({'result': 'room deleted'})

    return JsonResponse(
        {'error': 'cannot delete room (race started)'},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"message": "Пользователь успешно создан", "token": token.key},
                status=status.HTTP_201_CREATED
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"message": "Успешный вход", "token": token.key},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Неверные учетные данные"},
            status=status.HTTP_403_FORBIDDEN
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    return Response({
        'username': user.username,
        'mmr': user.mmr,
        'task_index': user.task_index,
    })
