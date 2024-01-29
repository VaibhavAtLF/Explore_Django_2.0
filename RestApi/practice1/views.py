from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def hello_world(resquest):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj,many = True)
    return Response({"status":200, "payload": serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    return Response({"status":201,"payload":data,"Msg":"hii"})