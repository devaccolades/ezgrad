from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from question.models import Questions,Options
from api.v1.question.serializers import QuestionsSerializer,OptionSerializer
from rest_framework.decorators import api_view
from general.functions import generate_serializer_errors

@api_view(['POST'])
def add_question(request):
    serialized_data=QuestionsSerializer(data=request.data)
    if serialized_data.is_valid():
        question=request.data['question']
        q=Questions.objects.create(question=question)
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
def view_question(request):
    question=Questions.objects.all()
    q=QuestionsSerializer(question,many=True)
    return Response({"Message":"True","response":q.data})

@api_view(['PUT'])
def edit_question(request,id):
    question=request.data.get('question')
    if(questions:=Questions.objects.filter(id=id)).exists():
        q=questions.latest('id')
        if question:
            q.question=question
        q.save()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Edited Successfully"
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
def delete_question(request,id):
    if(question:=Questions.objects.filter(id=id)).exists():
       q=question.latest('id')
       q.delete()
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
            "Data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


@api_view(['POST'])
def add_options(request):
    serialized_data = OptionSerializer(data=request.data)
    if serialized_data.is_valid():
        id=request.data['question']
        if (question:=Questions.objects.filter(id=id)).exists():
            questions=Questions.objects.get(id=id)
            options=request.data['options']
            option=Options.objects.create(
            question=questions,
            options=options
        )
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
def view_options(request):
    options=Options.objects.all()
    option=OptionSerializer(options,many=True)
    return Response({"Message":"True","response":option.data})

@api_view(['PUT'])
def edit_options(request,pk):
    options=request.data.get('options')
    if(option:=Options.objects.filter(pk=pk)).exists():
        opt=option.latest('id')
        if options:
            opt.options=options
        opt.save()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Edited Successfully"
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
def delete_options(request,pk):
    if(option:=Options.objects.filter(pk=pk)).exists():
        options=option.latest('id')
        options.delete()
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












