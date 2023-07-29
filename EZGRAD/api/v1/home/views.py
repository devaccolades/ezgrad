from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from home.models import Contact,Details,Experts,HomeDetails
from api.v1.home.serializers import ContactSerializer,DetailSerializer,ExpertSerializer,HomeDetailsSerializer
from rest_framework.decorators import api_view
from general.functions import generate_serializer_errors

@api_view(['POST'])
def add_homedetails(request):
    serialized_data=HomeDetailsSerializer(data=request.data)
    if serialized_data.is_valid():
        banner=request.data['main_banner']
        banner_url=request.data['main_banner_url']
        subbanner=request.data['sub_banner']
        subbanner_url=request.data['sub_banner_url']
        project_logo=request.data['project_logo']
        b=HomeDetails.objects.create(main_banner=banner,main_banner_url=banner_url,sub_banner=subbanner,sub_banner_url=subbanner_url,project_logo=project_logo)
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Successfully added"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":generate_serializer_errors(serialized_data._errors)
            }
        }
    return Response({'app_data':response_data})


@api_view(['GET'])
def view_homedetails(request):
    if (homedetails:=HomeDetails.objects.filter(is_deleted=False)).exists():
        serialized_data=HomeDetailsSerializer(homedetails,
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
def edit_homedetails(request,id):
    banner=request.data.get('main_banner')
    banner_url=request.data.get('main_banner_url')
    subbanner=request.data.get('sub_banner')
    subbanner_url=request.data.get('subbanner_url')
    project_logo=request.data.get('project_logo')
    if (home:=HomeDetails.objects.filter(id=id,is_deleted=False)).exists():
        homedata=home.latest('id')
        if banner:
            homedata.main_banner=banner
        if banner_url:
            homedata.main_banner_url=banner_url
        if subbanner:
            homedata.sub_banner=subbanner
        if subbanner_url:
            homedata.sub_banner_url=subbanner_url
        if project_logo:
            homedata.project_logo=project_logo
        homedata.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Edited Successfully"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})

@api_view(['DELETE'])
def delete_homedetails(request,id):
    if (home:=HomeDetails.objects.filter(id=id,is_deleted=False)).exists():
        homedetails=home.latest('id')
        homedetails.is_deleted=True
        homedetails.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Deleted Successfully"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not found"
            }
        }
    return Response({'app_data':response_data})


@api_view(['POST'])
def add_contact(request):
    serialized_data=ContactSerializer(data=request.data)
    if serialized_data.is_valid():
        logo=request.data['logo']
        about=request.data['about']
        address=request.data['address']
        phone=request.data['phone']
        email=request.data['email']
        facebook_url=request.data['facebook_url']
        instagram_url=request.data['instagram_url']
        youtube_url=request.data['youtube_url']
        whatsapp_url=request.data['whatsapp_url']
        linkedln_url=request.data['linkedln_url']

        contact=Contact.objects.create(logo=logo,
                                       about=about,
                                       address=address,
                                       phone=phone,
                                       email=email,
                                       facebook_url=facebook_url,
                                       instagram_url=instagram_url,
                                       youtube_url=youtube_url,
                                       whatsapp_url=whatsapp_url,
                                       linkedln_url=linkedln_url
                                       )
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"SUccessfully Added"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":generate_serializer_errors(serialized_data._errors)
            }
        }
    return Response({'app_data':response_data})


@api_view(['GET'])
def view_contact(request):
    if (contact:=Contact.objects.filter(is_deleted=False)).exists():
        serialized_data=ContactSerializer(contact,
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
def edit_contact(request,id):
    logo=request.data.get('logo')
    about=request.data.get('about')
    address=request.data.get('address')
    phone=request.data.get('phone')
    email=request.data.get('email')
    facebook_url=request.data.get('facebook_url')
    instagram_url=request.data.get('instagram_url')
    youtube_url=request.data.get('youtube_url')
    whatsapp_url=request.data.get('whatsapp_url')
    linkedln_url=request.data.get('whatsapp_url')
    if (c:=Contact.objects.filter(id=id,is_deleted=False)).exists():
        contact=c.latest('id')
        if logo:
            contact.logo=logo
        if about:
            contact.about=about
        if address:
            contact.address=address
        if phone:
            contact.phone=phone
        if email:
            contact.email=email
        if facebook_url:
            contact.facebook_url=facebook_url
        if instagram_url:
            contact.instagram_url=instagram_url
        if youtube_url:
            contact.youtube_url=youtube_url
        if whatsapp_url:
            contact.whatsapp_url=whatsapp_url
        if linkedln_url:
            contact.linkedln_url=linkedln_url
        contact.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Successfully Edited"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


@api_view(['DELETE'])
def delete_contact(request,id):
    if (c:=Contact.objects.filter(id=id,is_deleted=False)).exists():
        contact=c.latest('id')
        contact.is_deleted=True
        contact.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
            "title":"Success",
            "Message":"Deleted Successfully"
            }
        }
    else:
        response_data={
             "StatusCode" : 6001,
            "data":
            {
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


@api_view(['POST'])
def add_details(request):
    serialized_data=DetailSerializer(data=request.data)
    if serialized_data.is_valid():
        heading=request.data['heading']
        body=request.data['body']
        image=request.data['image']
        title=request.data['title']
        content=request.data['content']
        details=Details.objects.create(heading=heading,body=body,image=image,title=title,content=content)
        response_data={
            "StatusCode" : 6000,
            "data":
            {
                "title":"Success",
                "Message":"Added Successfully"
            
            }
        }
    else:
        response_data={
             "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":generate_serializer_errors(serialized_data._errors)
            }
        }
    return Response({'app_data':response_data})


@api_view(['GET'])
def view_details(request):
    if (details:=Details.objects.filter(is_deleted=False)).exists():
        serialized_data=DetailSerializer(details,
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
def edit_details(request,id):
    heading=request.data.get('heading')
    body=request.data.get('body')
    title=request.data.get('title')
    content=request.data.get('content')
    image=request.data.get('image')
    if (details:=Details.objects.filter(id=id,is_deleted=False)).exists():
        D=details.latest('id')
        if heading:
            D.heading=heading
        if body:
            D.body=body
        if title:
            D.title=title
        if content:
            D.content=content
        if image:
            D.image=image
        D.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Edited Successfully"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})

    
@api_view(['DELETE'])
def delete_details(request,id):
    if (d:=Details.objects.filter(id=id,is_deleted=False)).exists():
        details=d.latest('id')
        details.is_deleted=True
        details.save()
        response_data={
             "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Deleted Successfully"
            }
        }
    else:
        response_data={
             "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


@api_view(['POST'])
def add_experts(request):
    serialized_data=ExpertSerializer(data=request.data)
    if serialized_data.is_valid():
        title=request.data['title']
        content=request.data['content']
        name=request.data['name']
        role=request.data['role']
        experience=request.data['experience']
        photo=request.data['photo']
        rating=request.data['rating']
        counselling=request.data['counselling']
        exp=Experts.objects.create(
            title=title,
            content=content,
            name=name,
            role=role,
            experience=experience,
            photo=photo,
            rating=rating,
            counselling=counselling,
        )
        response_data={
             "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Added Successfully"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":
            {
                "title":"Failed",
                "Message":generate_serializer_errors(serialized_data._errors)
            }
        }
    return Response({'app_data':response_data})



@api_view(['GET'])
def view_experts(request):
    if (expert:=Experts.objects.filter(is_deleted=False)).exists():
        serialized_data=ExpertSerializer(expert,
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
def edit_experts(request,id):
    title=request.data.get('title')
    content=request.data.get('content')
    name=request.data.get('name')
    role=request.data.get('role')
    experience=request.data.get('experience')
    photo=request.data.get('photo')
    rating=request.data.get('rating')
    counselling=request.data.get('counselling')
    if (exp:=Experts.objects.filter(id=id,is_deleted=False)).exists():
        expert=exp.latest('id')
        if title:
            expert.title=title
        if content:
            expert.content=content
        if name:
            expert.name=name
        if role:
            expert.role=role
        if experience:
            expert.experience=experience
        if photo:
            expert.photo=photo
        if rating:
            expert.rating=rating
        if counselling:
            expert.counselling=counselling
        expert.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Edited Successfully"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})



@api_view(['DELETE'])
def delete_experts(request,id):
    if (exp:=Experts.objects.filter(id=id,is_deleted=False)).exists():
        expert=exp.latest('id')
        expert.is_deleted=True
        expert.save()
        response_data={
            "StatusCode" : 6000,
            "data":{
                "title":"Success",
                "Message":"Deleted Successfully"
            }
        }
    else:
        response_data={
            "StatusCode" : 6001,
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})


















