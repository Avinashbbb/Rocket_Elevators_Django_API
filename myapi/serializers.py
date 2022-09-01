# serializers.py
from attr import fields
from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id','firstnname','lastname','title','user_id','updated_at','created_at','facial_keypoints')