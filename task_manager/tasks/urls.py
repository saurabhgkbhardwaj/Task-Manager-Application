

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index, create_task, update_task

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create_task'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('api/', include(router.urls)),
]
