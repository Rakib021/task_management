from rest_framework import serializers
from .models import TaskStoreModel

class TaskStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStoreModel
        fields = '__all__'