from rest_framework import viewsets

from .serializers import WorkSpaceSerializer
from .models import WorkSpace
from .permissions import IsOwnerOrAdminOrDirector


class WorkSpaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSpaceSerializer
    queryset = WorkSpace.objects.all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve', 'destroy']:
            return [IsOwnerOrAdminOrDirector()]
        return super().get_permissions()
