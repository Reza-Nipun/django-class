from django.views.generic import View
from django.http import JsonResponse


class HealthCheck(View):
    def get(self, request):
        data = {
            'success': True,
            'message': 'This is the test view',
            'method': request.method,
        }
        return JsonResponse(data=data, status=200)
