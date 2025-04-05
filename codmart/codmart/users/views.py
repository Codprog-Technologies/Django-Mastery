from rest_framework import status, views, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users import models, serializers


# Create your views here.

@api_view(['POST'])
def create_user_api(request):
    # request.method / request.POST
    # request.data
    # return Response()
    if request.method == 'POST':
        # user = models.User.objects.create_user(**request.data)
        # request.data['id'] = user.pk
        # request.data.pop('password')
        # return Response(request.data, status=status.HTTP_201_CREATED)
        # deserialization and validation -> request.data -> user
        # serialization -> user -> dict
        serializer = serializers.UserSerializer(data=request.data)  # deserialization and validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # serialization
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateUserView(views.APIView):
#     def post(self, request):
#         serializer = serializers.UserSerializer(data=request.data)  # deserialization and validation
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # serialization
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class DestroyUserView(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UpdateUserView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserUpdateSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserUpdateSerializer


class ListCreateUserView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
