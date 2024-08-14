from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from AuthApp.serializers import LoginSerializer, LoggedInUserSerializer
from rest_framework import generics
from AuthApp.models import UserPhoneNumber
from django.utils import timezone

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']

            try:
                user_phone = UserPhoneNumber.objects.get(phone_number=phone_number)

                if user_phone.is_password_valid(password):
                    return Response({
                        'message': 'Muvofaqqiyatli Login qilindi',
                        'user_id': user_phone.id,
                        'phone_number': user_phone.phone_number,
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'error': 'Kod xato yoki muddati o\'tgan'
                    }, status=status.HTTP_400_BAD_REQUEST)
            except UserPhoneNumber.DoesNotExist:
                return Response({
                    'error': 'Telfon raqam topilmadi'
                }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoggedInUsersView(generics.ListAPIView):
    queryset = UserPhoneNumber.objects.all()
    serializer_class = LoggedInUserSerializer

    def get_queryset(self):
        return UserPhoneNumber.objects.filter(password_expiry__gt=timezone.now())