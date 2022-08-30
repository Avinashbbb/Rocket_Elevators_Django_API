# serializers.py
from attr import fields
from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('id','firstnname','lastname','title','user_id','created_at','updated_at','facial_keypoints')