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
from general.decorators import group_required

@api_view(['POST'])
@group_required(['ezgrad_admin'])
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
@group_required(['ezgrad_admin'])
def view_service(request):
    if (service:=ServiceType.objects.filter(is_deleted=False)).exists():
        serialized_data=ServiceSerializer(service,
                                          context={
                                              "request":request,
                                          },
                                          many=True,).data
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "data":serialized_data
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
    


@api_view(['PUT'])
@group_required(['ezgrad_admin'])
def edit_service(request,pk):
    service=request.data.get('service')
    if(services:=ServiceType.objects.filter(pk=pk,is_deleted=False)).exists():
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
@group_required(['ezgrad_admin'])
def delete_service(request,pk):
    if(service:=ServiceType.objects.filter(pk=pk,is_deleted=False)).exists():
        s=service.latest('id')
        s.is_deleted=True
        s.save()
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


@api_view(['GET'])
def list_service(request):
    if (service:=ServiceType.objects.filter(is_deleted=False)).exists():
        serialized_data=ServiceSerializer(service,
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
            "StatusCode":6000,
            "data":[]
        }
    return Response({'app_data':response_data})





@api_view(['POST'])
@group_required(['ezgrad_admin'])
def add_coursetype(request):
    serialized_data=CourseTypeSerializer(data=request.data)
    if serialized_data.is_valid():
        pk=request.data['service']
        if(service:=ServiceType.objects.filter(id=pk,is_deleted=False)).exists():
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
                    "data":"Failed",
                    "Message":"Not Found"
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
@group_required(['ezgrad_admin'])
def view_coursetype(request):
    if (coursetype:=CourseType.objects.filter(is_deleted=False)).exists():
        serialized_data=CourseTypeSerializer(coursetype,
                                             context={
                                                 "request":request,
                                             },
                                             many=True,).data
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "data":serialized_data
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


@api_view(['PUT'])
@group_required(['ezgrad_admin'])
def edit_coursetype(request,id):
    coursetype=request.data.get('course_type')
    if(coursetypes:=CourseType.objects.filter(id=id,is_deleted=False)).exists():
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
@group_required(['ezgrad_admin'])
def delete_coursetype(request,id):
    if(coursetypes:=CourseType.objects.filter(id=id,is_deleted=False)).exists():
        c=coursetypes.latest('id')
        c.is_deleted=True
        c.save()
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

    
@api_view(['GET'])
def list_coursetype(request):
    service=request.data.get('service')
    if (services:=ServiceType.objects.filter(id=service,is_deleted=False)).exists():
        s=services.latest('id')
        if (coursetype:=CourseType.objects.filter(service=s,is_deleted=False)).exists():
            serialized_data=CourseTypeSerializer(coursetype,
                                              context={
                                                  'request':request,
                                              },
                                              many=True,).data
        
            response_data={
                "StatusCode":6000,
                "CourseType":serialized_data
                  }
                
        else:
            response_data={
                "StatusCode":6000,
                "data":[]
            }
    else:
        response_data={
            "StatusCode":6000,
            "data":[]
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

