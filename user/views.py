from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserSerializers, UserLoginSerializer


# @api_view(['POST'])
# def register(request):
#     if request.user.is_authenticated:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     serializer = UserSerializers(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#         return Response(status=status.HTTP_201_CREATED)
#
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User registered successfully"})


class Login(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(usename=username, password=password)

        if user is None:
            return Response(data={"error": "invalid authent"}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        return Response(status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Logout(request)

        return Response(status=status.HTTP_200_OK)
