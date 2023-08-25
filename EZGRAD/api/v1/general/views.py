from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from general.models import StudentProfile,ChiefProfile,ReviewStudent
from course.models import Country
from question.models import RecordAnswer,Options
from api.v1.question.serializers import RecordAnswerSerializer,OptionSerializer
from api.v1.general.serializers import StudentProfileSerializer,ReviewStudentSerializer,AddStudentProfileSerializer,ChiefProfileSerializer,LoginSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from general.functions import generate_serializer_errors,check_username,randomnumber
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from general.encryption import encrypt, decrypt
from rest_framework import status
import requests
import json
from general.decorators import group_required


@api_view(['POST'])
def register_student(request):
    serialized_data=AddStudentProfileSerializer(data=request.data)
    if serialized_data.is_valid():
        name=request.data['name']
        email=request.data['email']
        mobile=request.data['mobile']
        gender=request.data['gender']
        dob=request.data['dob']

        if (reg:=StudentProfile.objects.filter(name=name,email=email,mobile=mobile,gender=gender,dob=dob)).exists():
             return Response({"Message":"Already Exists"})
        else:
            student_profile=StudentProfile.objects.create(name=name,email=email,mobile=mobile,gender=gender,dob=dob)

            password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")
            sliced_phone = mobile[-4:]
            username = f'EZG{sliced_phone}{randomnumber(4)}'
            username = check_username(username)
                        
            user = User.objects.create_user(
                            username=username,
                            password=password
                        ) 
            student_profile.user = user
            student_profile.username = username
            student_profile.password = password                  
            student_profile.save()

            student_group, created = Group.objects.get_or_create(name='ezgrad_student')
            student_group.user_set.add(user)

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
@group_required(['ezgrad_student'])
def view_studentprofile(request):
    if (reg:=StudentProfile.objects.filter(is_deleted=False)).exists():
        serialized_data=StudentProfileSerializer(reg,
                                           context={
                                               "request":request,
                                           },
                                           many=True,).data
        response_data={
            "StatusCode":6000,
            "data":serialized_data
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

@api_view(['PUT'])
@group_required(['ezgrad_student'])
def edit_studentprofile(request,pk):
    name=request.data.get('name')
    email=request.data.get('email')
    mobile=request.data.get('mobile')
    if(register:=StudentProfile.objects.filter(pk=pk)).exists():
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
                "title":"Success",
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
@group_required(['ezgrad_admin'])
def delete_studentprofile(request,pk):
    if(reg:=StudentProfile.objects.filter(pk=pk,is_deleted=False)).exists():
        register=reg.latest('id')
        register.is_deleted=True
        register.save()
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

@api_view(['GET'])
@group_required(['ezgrad_student'])
def list_studentdetails(request,pk):
     if (student:=StudentProfile.objects.filter(pk=pk,is_deleted=False)).exists():
          serialized_data=StudentProfileSerializer(student,
                                                   context={
                                                        "request":request,
                                                   },many=True,).data
          response_data={
               "StatusCode":6000,
               "data":serialized_data
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

@api_view(['GET'])
@group_required(['ezgrad_student'])
def list_studentprofile(request,pk):
     if (record:=RecordAnswer.objects.filter(userid=pk,is_deleted=False)).exists():
          serialized_data=RecordAnswerSerializer(record,
                                                 context={
                                                      'request':request,
                                                 },
                                                 many=True,).data
          response_data={
               "StatusCode":6000,
               "data":serialized_data
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


@api_view(['POST'])
@group_required(['ezgrad_student'])
def update_selected_option(request,pk):
    record_answer=request.data.get('updated_records')
    if record_answer:
        for i in record_answer:
            id=i['recordid']
            value=i['updated_value']
            if (recordanswer:=RecordAnswer.objects.filter(userid=pk,id=id,is_deleted=False)).exists():
                    for i in record_answer:
                        id=i['recordid']
                        value=i['updated_value']
                        if (options:=RecordAnswer.objects.filter(pk=id,is_deleted=False)).exists():
                            option = options.latest("id")
                            if option:
                                new_option1 = Options.objects.get(id=value)
                                option.option=new_option1
                                option.save()
                    response_data={
                        "StatusCode":6000,
                        "data":{
                                "title":"Success",
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
    else:
        response_data={
                  "StatusCode":6001,
                  "data":{
                       "title":"Failed",
                       "Message":"Not Found"
                  }
             }
    return Response({'app_data':response_data})
                    
        
@api_view(['POST'])
@group_required(['ezgrad_admin'])
def create_chief_user(request):
    serialized_data=ChiefProfileSerializer(data=request.data)
    if serialized_data.is_valid():
        username=request.data['username']
        password=request.data['password']
        confirm_password=request.data['confirm_password']
        if password==confirm_password:
            set_password=password
            if not ChiefProfile.objects.filter(username=username,password=password).exists():
                 user = User.objects.create_user(
                            username=username,
                            password=password
                        ) 
                 chief_user= ChiefProfile.objects.create(username=username,
                                        password=password,
                                        user=user
                                        )
                 group_name='ezgrad_admin'
                 chief_group, created = Group.objects.get_or_create(name=group_name)
                 chief_group.user_set.add(user)
                 group_name='ezgrad_admin'
                 response_data={
                     "StatusCode":6000,
                     "data":{
                         "title":"Success",
                         "Message":"Chief user created successfully"
                     }
                 }
            else:
                response_data={
                    "StatusCode":6001,
                    "data":{
                        "title":"Failed",
                        "Message":"Chief user already exist"
                    }
                }
        else:
            response_data={
                "StatusCode":6001,
                "data":{
                    "title":"Failed",
                    "Message":"password didn't Match"
                }
            }
    else:
        response_data={
            "StatusCode":6001,
            "data":{
                "title":"Validation error",
                "Message":generate_serializer_errors(serialized_data._errors)
            }
        }
    return Response({'app_data':response_data})


@api_view(['POST'])
@permission_classes([AllowAny])
def chief_login(request):
    serialized_data=ChiefProfileSerializer(data=request.data)
    if serialized_data.is_valid():
        username=request.data['username']
        password=request.data['password']
        if ChiefProfile.objects.filter(username=username,is_deleted=False).exists():
            profile=ChiefProfile.objects.get(username=username,is_deleted=False)
            if profile.password==password:
                protocol="http://"
                if request.is_secure():
                    protocol="https://"
                web_host = request.get_host()
                request_url = protocol + web_host + "/api/token/"
                login_response = requests.post(
                        request_url,
                        data={
                            'username': profile.user.username,
                            'password': password,
                        }
                    )
                if login_response.status_code == 200:
                        login_response = login_response.json()

                        response_data = {
                            "StatusCode": 6000,
                            "data" : {
                                "title": "Success!",
                                "message": "Success!",
                                "access_token": login_response["access"],
                                "refresh_token": login_response["refresh"],
                            },
                        }
                else:
                        response_data = {
                            "StatusCode": 6001,
                            "data" : {
                                "title": "Failed!",
                                "message": "Token generation failed",
                                "login_status_code" :  login_response.status_code
                            },
                        }
            else:
                    response_data = {
                        "StatusCode": 6001,
                        "data" : {
                            "title": "Failed",
                            "message": "Password is incorrect",
                        },
                    }
        else:
                response_data = {
                    "StatusCode": 6001,
                    "data" : {
                        "title": "Failed",
                        "message": "User Not Exists"
                    },
                }
    else:
            response_data = {
                "StatusCode": 6001,
                "data": {
                    "title": "Validation Error",
                    "message": generate_serializer_errors(serialized_data._errors)
                }
            }
    return Response({'app_data' : response_data}, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([AllowAny])
@group_required(['ezgrad_student'])
def student_login(request):
     serialized_data=LoginSerializer(data=request.data)
     if serialized_data.is_valid():
        mobile=request.data['mobile']
        if StudentProfile.objects.filter(mobile=mobile,is_deleted=False).exists():
             student_profile=StudentProfile.objects.get(mobile=mobile,is_deleted=False)
             headers = {
                    "Content-Type": "application/json"
                }
             username = student_profile.user.username
             password = student_profile.password
             data = {
                    "username": username,
                    "password": password,
                }
             protocol = "http://"
             if request.is_secure():
                    protocol = "https://"

             host = request.get_host()

             url = protocol + host + "/api/token/"
             response = requests.post(url, headers=headers, data=json.dumps(data))
             if response.status_code == 200:
                    response = response.json()
                    response_data = {
                        "StatusCode": 6000,
                        "data": {
                            "title": "Success",
                            "message": "Login successfully.",
                            "phone": mobile,
                            "access_token" : response["access"],
                            "refresh_token" : response["refresh"],
                        }
                    }
             else:
                    response_data = {
                        "StatusCode": 6001,
                        "data": {
                            "title": "Failed",
                            "message": "Token generation failed."
                        }
                    }
        else:
                response_data = {
                    "StatusCode": 6001,
                    "data" : {
                        "title": "Failed!",
                        "message": "User Not found"
                    },
                }
     else:
            response_data = {
                "StatusCode": 6001,
                "data" : {
                    "title": "Validation Error",
                    "message": generate_serializer_errors(serialized_data._errors)
                },
            }

     return Response({'app_data' : response_data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@group_required(['ezgrad_student'])
def save_student_review(request):
     serialized_data=ReviewStudentSerializer(data=request.data)
     if serialized_data.is_valid():
          name=request.POST['name']
          rating=request.POST['rating']
          review=request.POST['review']
          student_review=ReviewStudent.objects.create(name=name,
                                                      rating=rating,
                                                      review=review)
          response_data={
               "StatusCode":6000,
               "data":{
                    "title":"Success",
                    "Message":"Added Successfully"
               }
          }
     else:
          response_data={
               "StatusCode":6001,
               "data":{
                    "title":"Failed",
                    "Message":generate_serializer_errors(serialized_data._errors)
               }
          }
     return Response({'app_data':response_data})
     

@api_view(['GET'])
def list_student_review(request):
     if (student:=ReviewStudent.objects.filter(is_deleted=False)).exists():
          serialized_data=ReviewStudentSerializer(student,
                                        context={
                                             "request":request,
                                        },
                                        many=True,).data
          response_data={
               "StatusCode":6000,
               "data":serialized_data
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



