from tkinter import Image
from django.http import JsonResponse
from .models import Employees
from .serializers import EmployeesSerializer
from myapi import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import face_recognition
import cv2
import numpy as np
from PIL import Image

def employee_list(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET','POST'])
def employee_detail(request):
    incomingImg = Image.open(request.data['photo'])
    img_numpy_arr = np.array(incomingImg)
    encodedincomingImg = face_recognition.face_encodings(img_numpy_arr)[0]

    employees = Employees.objects.all()
    
    for i in employees:
        print(i.id)
        encodedemployeeImg = np.array(i.facial_keypoints)
        if (face_recognition.compare_faces([encodedincomingImg], encodedemployeeImg)):
            employee =  Employees.objects.get(pk = i.id)
            serializer = EmployeesSerializer(employee)
            output = JsonResponse(serializer.data, safe=False)
            return output
        else :
            return JsonResponse(status=404, data={'status':'false','message':"No Employee match our record"})