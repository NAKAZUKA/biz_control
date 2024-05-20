from rest_framework.permissions import BasePermission


class IsOwnerOrAdminOrDirector(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'owner']:
            return True
        if hasattr(obj, 'director') and obj.director == request.user:
            return True
        return False
