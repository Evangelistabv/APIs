from rest_framework.views import APIView
from rest_framework import generics,permissions,serializers
from .models import UserData
from .serializers import UserSerializer,UserLoginSerializer
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserDetailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = UserData.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data['username_or_email']
            password = serializer.validated_data['password']

            user = UserData.objects.filter(name=username_or_email).first()
            if not user:
                user = UserData.objects.filter(email=username_or_email).first()
                if not user:
                    return Response({"error": "Username or email not found."}, status=status.HTTP_404_NOT_FOUND)

            if not user.check_password(password):
                return Response({"error": "Incorrect password."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                "message": "Login successful.",
                "username": user.name,
                "email": user.email
            }, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
