from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet,basename="task")



urlpatterns = [
   
    path('', include(router.urls)),
    path('tasks/',views.taskitems,name='task_list'),
    
]