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
    details=HomeDetails.objects.all()
    b=HomeDetailsSerializer(details,many=True)
    return Response({"Message":"True","response":b.data})

@api_view(['PUT'])
def edit_homedetails(request,id):
    banner=request.data.get('main_banner')
    banner_url=request.data.get('main_banner_url')
    subbanner=request.data.get('sub_banner')
    subbanner_url=request.data.get('subbanner_url')
    project_logo=request.data.get('project_logo')
    if (b:=HomeDetails.objects.filter(id=id)).exists():
        B=b.latest('id')
        if banner:
            B.main_banner=banner
        if banner_url:
            B.main_banner_url=banner_url
        if subbanner:
            B.sub_banner=subbanner
        if subbanner_url:
            B.sub_banner_url=subbanner_url
        if project_logo:
            B.project_logo=project_logo
        B.save()
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
    if (b:=HomeDetails.objects.filter(id=id)).exists():
        B=b.latest('id')
        B.delete()
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
    contact=Contact.objects.all()
    c=ContactSerializer(contact,many=True)
    return Response({'Message':True,"response":c.data})

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
    if (c:=Contact.objects.filter(id=id)).exists():
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
    if (c:=Contact.objects.filter(id=id)).exists():
        contact=c.latest('id')
        contact.delete()
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
    details=Details.objects.all()
    d=DetailSerializer(details,many=True)
    return Response({"Message":True,"response":d.data})

@api_view(['PUT'])
def edit_details(request,id):
    heading=request.data.get('heading')
    body=request.data.get('body')
    title=request.data.get('title')
    content=request.data.get('content')
    image=request.data.get('image')
    if (details:=Details.objects.filter(id=id)).exists():
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
    if (details:=Details.objects.filter(id=id)).exists():
        d=details.latest('id')
        d.delete()
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
    expert=Experts.objects.all()
    exp=ExpertSerializer(expert,many=True)
    return Response({"Message":"True","response":exp.data})

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
    if (exp:=Experts.objects.filter(id=id)).exists():
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
    if (exp:=Experts.objects.filter(id=id)).exists():
        expert=exp.latest('id')
        expert.delete()
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


















