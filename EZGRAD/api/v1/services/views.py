from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from services.models import ServiceType,CourseType
from api.v1.services.serializers import ServiceSerializer,CourseTypeSerializer
from rest_framework.decorators import api_view
from general.functions import generate_serializer_errors
from rest_framework import status

@api_view(['POST'])
def add_service(request):
    serialized_data=ServiceSerializer(data=request.data)
    if serialized_data.is_valid():
        service=request.data['service']
        s=ServiceType.objects.create(service=service)
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Successfully Added"
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
def view_service(request):
    service=ServiceType.objects.all()
    s=ServiceSerializer(service,many=True)
    return Response({"Message":"True","response":s.data})

@api_view(['PUT'])
def edit_service(request,pk):
    service=request.data.get('service')
    if(services:=ServiceType.objects.filter(pk=pk)).exists():
        s=services.latest('id')
        if service:
            s.service=service
        s.save()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Successfully Edited"
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
def delete_service(request,pk):
    if(service:=ServiceType.objects.filter(pk=pk)).exists():
        s=service.latest('id')
        s.delete()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Deleted Successfully"
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
def add_coursetype(request):
    serialized_data=CourseTypeSerializer(data=request.data)
    if serialized_data.is_valid():
        pk=request.data['service']
        if(service:=ServiceType.objects.filter(id=pk)).exists():
            service_data=ServiceType.objects.get(pk=pk)
            course_type=request.data['course_type']
            c=CourseType.objects.create(course_type=course_type,service=service_data)
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
def view_coursetype(request):
    coursetype=CourseType.objects.all()
    course=CourseTypeSerializer(coursetype,many=True)
    return Response({"Message":"True","response":course.data})


@api_view(['PUT'])
def edit_coursetype(request,id):
    coursetype=request.data.get('course_type')
    if(coursetypes:=CourseType.objects.filter(id=id)).exists():
        c=coursetypes.latest('id')
        if coursetype:
            c.course_type=coursetype
        c.save()
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
def delete_coursetype(request,id):
    if(coursetypes:=CourseType.objects.filter(id=id)).exists():
        c=coursetypes.latest('id')
        c.delete()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Deleted Successfully"
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

    













# @api_view(['POST','GET'])
# def test(request):
#     print(request.POST)
#     print(request.data)
#     print(request.GET)
#     # v=request.data
#     # for i in v:
#     #     print("question=" + i["question"] + "answer="+ i["ans"])

#     return Response({'app_data':"True"})

