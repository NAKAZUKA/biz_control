# work_space/permissions.py
from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object or admins to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user and request.user.is_staff:
            return True

        # Check if the user is the owner of the object
        return obj.director == request.user
