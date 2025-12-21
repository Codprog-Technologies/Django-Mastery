from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class HealthCheckView(APIView):

    def get(self, request):
        # 200 -> healthy
        # 500 -> unhealthy
        try:
            connection.ensure_connection()
        except Exception:
            return Response({'status': 'DB Connection Issue'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'status': 'ok'})
