from .models import TaskStoreModel
from .serializers import TaskStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = TaskStoreModel.objects.all()
    serializer_class = TaskStoreSerializer


def taskitems(request):
    return render(request,'tasks.html')