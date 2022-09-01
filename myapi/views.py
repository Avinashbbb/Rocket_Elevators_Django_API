from tkinter import Image
from attr import attributes
from django.http import JsonResponse
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import face_recognition
import numpy as np
from PIL import Image
from datetime import datetime
import json


def employee_list(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET','POST'])
def employee_detail(request):
    if request.method =='GET':
        incomingImg = Image.open(request.data['photo'])
        img_numpy_arr = np.array(incomingImg)
        encodedincomingImg = face_recognition.face_encodings(img_numpy_arr)[0]
        employees = Employees.objects.all()
        for i in employees:
            encodedemployeeImg = np.array(i.facial_keypoints)
        if (face_recognition.compare_faces([encodedincomingImg], encodedemployeeImg)):
            employee =  Employees.objects.get(pk = i.id)
            serializer = EmployeesSerializer(employee)
            output = JsonResponse(serializer.data, safe=False)
            return output
        else :
            return JsonResponse(status=404, data={'status':'false','message':"No Employee match our record"})

    if request.method == 'POST':
        incomingImg = Image.open(request.data['photo'])
        img_numpy_arr = np.array(incomingImg)
        encodedincomingImg = face_recognition.face_encodings(img_numpy_arr)[0]
        employees = Employees.objects.all()
        employee = Employees()
        attributes ={
            'firstnname' : request.data['firstnname'],
            'lastname' : request.data['lastname'],
            'title' : request.data['title'],
            # 'user_id' : request.data['user_id'],
            'updated_at' : datetime.now(),
            'created_at' : datetime.now(),
            'facial_keypoints' : encodedincomingImg
        }
        employee.__setattr__('firstnname', attributes['firstnname'])
        employee.__setattr__('lastname', attributes['lastname'])
        employee.__setattr__('title', attributes['title'])
        employee.__setattr__('updated_at', attributes['updated_at'])
        employee.__setattr__('created_at', attributes['created_at'])
        employee.__setattr__('facial_keypoints', encodedincomingImg.tolist())
        employee.save()            
        return Response(attributes, status = status.HTTP_201_CREATED)
