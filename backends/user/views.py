from rest_framework import viewsets
from rest_framework.permissions import BasePermission, AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve']:
            return [IsOwnerOrAdmin()]
        return super().get_permissions()
