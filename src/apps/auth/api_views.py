from .serializers import (
    RegistrarUsuarioSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
)

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

#from rest_condition import And, Or
#from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

token_generator = PasswordResetTokenGenerator()

#ViewSet para registrar usuários.
class RegistrarUsuarioViewSet(viewsets.ModelViewSet):

    serializer_class = RegistrarUsuarioSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Usuário cadastrado com sucesso"
        }, status=status.HTTP_201_CREATED)

#Viewst para Requst do Pass
class PasswordResetRequestView(viewsets.ModelViewSet):
    serializer_class = PasswordResetRequestSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        msg = "Se o e-mail existir, enviaremos instruções para redefinir a senha."
        email = serializer.validated_data["email"].strip().lower()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": msg}, status=status.HTTP_200_OK)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        frontend_url = getattr(settings, "FRONTEND_URL", "http://localhost:5173")
        reset_link = f"{frontend_url}/reset-password?uid={uid}&token={token}"

        subject = "Redefinição de senha"
        body = (
            f"Olá,\n\nUse o link para redefinir sua senha:\n{reset_link}\n\n"
            "Se você não solicitou, ignore este e-mail."
        )
        send_mail(
            subject,
            body,
            getattr(settings, "DEFAULT_FROM_EMAIL", "no-reply@example.com"),
            [email],
            fail_silently=True,
        )

        return Response({"detail": msg}, status=status.HTTP_200_OK)

#Viewst para Confirm do Pass
class PasswordResetConfirmView(viewsets.ModelViewSet):
    serializer_class = PasswordResetConfirmSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = serializer.validated_data["uid"]
        token = serializer.validated_data["token"]
        new_password = serializer.validated_data["new_password"]

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            return Response({"detail": "Link inválido."}, status=status.HTTP_400_BAD_REQUEST)

        if not token_generator.check_token(user, token):
            return Response({"detail": "Token inválido ou expirado."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_active": user.is_active,
    })