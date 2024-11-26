from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from .serializers import *
from .models import *
from .task_generator import TaskGenerator


def leaderboard_view(request):
    users = User.objects.order_by('-mmr')[:10]
    serializer = UserSerializer(users, many=True)

    return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


def enemy_view(request):
    user = User.objects.get(username=request.GET['username'])
    try:
        room = (Room.objects.filter(first_user=user) or Room.objects.filter(second_user=user)).first()
        enemy = room.first_user if room.first_user != user else room.second_user

        return JsonResponse(
            data={
                'result': 'race is going',
                'float': (enemy.task_index + 1) / 10
            }, status=status.HTTP_200_OK
        )


    except Room.DoesNotExist:
        return JsonResponse(
            data={
                'result': 'lose',
                'difference': 10
            }, status=status.HTTP_200_OK
        )


def answer_view(request):
    try:
        answer = float(request.GET['answer'])
    except ValueError:
        return JsonResponse(
            {'error': 'answer must be an integer (or float)'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.get(username=request.GET['username'])
    room = (Room.objects.filter(first_user=user) or Room.objects.filter(second_user=user)).first()
    enemy = room.first_user if room.first_user != user else room.second_user

    tasks = RoomTask.objects.filter(room=room).order_by('id')

    current_task = tasks[user.task_index]

    if current_task.answer == answer:
        user.task_index += 1
        user.save()

        if user.task_index == len(tasks):
            user.task_index = 0
            user.mmr = + 10
            user.save()

            enemy.task_index = 0
            enemy.mmr = - 10
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
            data={'result': 'good answer'},
            status=status.HTTP_200_OK
        )

    return JsonResponse(
        data={'result': 'bad answer'},
        status=status.HTTP_200_OK
    )


class RoomView(APIView):
    def get(self, request):
        user = User.objects.get(username=request.GET['username'])

        try:
            task_count = int(request.GET['task_count'])

            if not 5 <= task_count <= 20:
                raise ValueError
        except KeyError:
            return JsonResponse(
                data={"error": "task_count param is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValueError:
            return JsonResponse(
                data={"error": "task_count must be an integer between 5 and 20"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            room = Room.objects.get(first_user=user)
            current_task = RoomTask.objects.all(room=room).order_by('id')[user.task_index]
            if room.second_user is not None:
                data = {
                    'result': 'joined',
                    'other_user': UserSerializer(room.second_user).data,
                    'task_text': current_task.text
                }
            else:
                data = {
                    'result': 'waiting'
                }

        except Room.DoesNotExist:
            available_rooms = Room.objects.filter(second_user__isnull=True, task_count=task_count)
            if available_rooms.exists():
                room = available_rooms.first()
                room.second_user = user
                room.save()

                current_task = RoomTask.objects.all(room=room).order_by('number')[user.task_index]

                data = {
                    'result': 'joined',
                    'other_user': UserSerializer(room.first).data,
                    'first_task': current_task.text
                }
            else:
                room = Room.objects.create(first_user=user, task_count=task_count)

                for i, (text, answer) in enumerate(TaskGenerator(task_count), 1):
                    RoomTask.objects.create(room=room, number=i, text=text, answer=answer)

                data = {
                    'result': 'created'
                }

        return JsonResponse(data=data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = User.objects.get(username=request.GET['username'])

        room = Room.objects.get(first_user=user)

        if room.second_user is None:
            Room.delete(room)
            return JsonResponse(data={'result': 'room deleted'}, status=status.HTTP_200_OK)

        return JsonResponse(
            data={'error': 'cannot delete room (race started)'},
            status=status.HTTP_400_BAD_REQUEST
        )


def get_task(request):
    return HttpResponse(
        '<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>\n'
        "\(\sqrt{b^2 - 4ac}\)",
    )
