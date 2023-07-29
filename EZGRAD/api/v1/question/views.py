from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from general.models import Register
from question.models import Questions,Options,RecordAnswer
from api.v1.question.serializers import QuestionsSerializer,OptionSerializer,RecordAnswerSerializer
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
    if (question:=Questions.objects.filter(is_deleted=False)).exists():
        serialized_data=QuestionsSerializer(question,
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
def edit_question(request,id):
    question=request.data.get('question')
    if(questions:=Questions.objects.filter(id=id,is_deleted=False)).exists():
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
    if(question:=Questions.objects.filter(id=id,is_deleted=False)).exists():
       q=question.latest('id')
       q.is_deleted=True
       q.save()
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
        if (question:=Questions.objects.filter(id=id,is_deleted=False)).exists():
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
    if (options:=Options.objects.filter(is_deleted=False)).exists():
        serialized_data=OptionSerializer(options,
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
def edit_options(request,pk):
    options=request.data.get('options')
    if(option:=Options.objects.filter(pk=pk,is_deleted=False)).exists():
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
    if(option:=Options.objects.filter(pk=pk,is_deleted=False)).exists():
        options=option.latest('id')
        options.is_deleted=True
        options.save()
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
def add_answer(request):
    serialized_data=RecordAnswerSerializer(data=request.data)
    if serialized_data.is_valid():
        userid=request.data.get('userid')
        option=request.data.get('option')
        if (reg:=Register.objects.filter(id=userid,is_deleted=False)).exists():
            user=Register.objects.get(id=userid)
        else:
            userid= None
        if (opt:=Options.objects.filter(id=option,is_deleted=False)).exists():
            options=Options.objects.get(id=option)
        else:
            option=None
        record=RecordAnswer.objects.create(userid=user,
                                           option=options,
                                          )
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
def view_answer(request):
    if (answer:=RecordAnswer.objects.filter(is_deleted=False)).exists():
        serialized_data=RecordAnswerSerializer(answer,
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
            "data":6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})

@api_view(['DELETE'])
def delete_answer(request,id):
    if (answer:=RecordAnswer.objects.filter(id=id,is_deleted=False)).exists():
        record=answer.latest('id')
        record.is_deleted=True
        record.save()
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Deleted Success"
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








        
        


    












