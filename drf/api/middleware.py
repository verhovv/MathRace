from django.http import JsonResponse
from django.shortcuts import redirect


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_paths = ['/api/login/', '/api/register/']

        if not request.user.is_authenticated and request.path not in public_paths:
            if request.headers.get('accept') == 'application/json':
                return JsonResponse({'error': 'Unauthorized'}, status=401)
            return redirect('login')

        response = self.get_response(request)
        return response
