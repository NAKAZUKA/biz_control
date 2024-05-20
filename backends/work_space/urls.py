from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkSpaceViewSet


router = DefaultRouter()
router.register(r'work_spaces', WorkSpaceViewSet, basename='work_spaces')


urlpatterns = [
    path('', include(router.urls)),
]
