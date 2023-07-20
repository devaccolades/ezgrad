from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from general.models import Register
from api.v1.general.serializers import RegisterSerializer,AddregisterSerializer
from rest_framework.decorators import api_view
from general.functions import generate_serializer_errors
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt



@api_view(['POST'])
def add_register(request):
    serialized_data=AddregisterSerializer(data=request.data)
    if serialized_data.is_valid():
        name=request.data['name']
        email=request.data['email']
        mobile=request.data['mobile']
        gender=request.data['gender']
        dob=request.data['dob']
        country=request.data['country']

        if (reg:=Register.objects.filter(name=name,email=email,mobile=mobile,gender=gender,dob=dob,
            country=country)).exists():
             return Response({"Message":"Already Exists"})
        else:
            Register.objects.create(name=name,email=email,mobile=mobile,gender=gender,dob=dob,
            country=country)
            response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Registered Successfully "

            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
            "title":"Failed",
            "Message": generate_serializer_errors(serialized_data._errors)
            }
        }
    return Response({'app_data':response_data})


@api_view(['GET'])
def view_register(request):
    reg=Register.objects.all()
    register=RegisterSerializer(reg,many=True)
    return Response({"Message":"True","response":register.data})

@api_view(['PUT'])
def edit_register(request,id):
    name=request.data.get('name')
    email=request.data.get('email')
    mobile=request.data.get('mobile')
    if(register:=Register.objects.filter(id=id)).exists():
        reg=register.latest('id')
        if name:
            reg.name=name
        if email:
            reg.email=email
        if mobile:
            reg.mobile=mobile
        reg.save()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Suceess",
                "Message":"Updated Successfully"
            }
        }
    else:
        response_data={
            "StatusCode":6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


@api_view(['DELETE'])
def delete_register(request,id):
    if(register:=Register.objects.filter(id=id)).exists():
        reg=register.latest('id')
        reg.delete()
        response_data={
            "data":{
                "title":"Success",
                "Message":"Deleted Successfully"
            }
        }
    else:
        response_data={
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


































































# @csrf_exempt
# def UserLogin(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     if User.objects.filter(username=username,password=password).exists():
#         u = User.objects.get(username=username,password=password)
#         if u.last_name == 'User':
#             f = Register.objects.filter(user_id=u.id)
#             s = RegisterSerializer(f,many=True)
#             return Response({"message":"True","response":"success"})
            
#         else:
#             return Response({"message":"True","response":"Invalid Username or password"})
#     else:
#         return Response({"message":"True","response":"Not Found"})



