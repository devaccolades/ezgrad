from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from course.models import University,Facts,Approval,Course,Country,CourseSpecialization,Faq
from services.models import CourseType,ServiceType
from api.v1.services.serializers import ServiceSerializer
from api.v1.course.serializers import UniversitySerializer,FactSerializer,CourseviewSerializer,FaqSerializer,ApprovalSerializer,CourseSerializer,CourseSpecializationSerializer,CountrySerializer
from rest_framework.decorators import api_view
from general.functions import generate_serializer_errors
from general.decorators import group_required

@api_view(['POST'])
@group_required(['ezgrad_admin'])
def add_university(request):
    serialized_data=UniversitySerializer(data=request.data)
    if serialized_data.is_valid():
        logo=request.data['university_logo']
        name=request.data['university_name']
        about=request.data['about_university']
        certificate=request.data['sample_certificate']
        prospectus=request.data['prospectus']
        coursetype=request.data['coursetype']
        country=request.data.get('country')
        if (coursetypes:=CourseType.objects.filter(id=coursetype)).exists():
            coursetypes=CourseType.objects.get(id=coursetype)
        else:
            coursetype=None
        university=University.objects.create(coursetype=coursetypes,
                                             university_logo=logo,
                                             university_name=name,
                                             about_university=about,
                                             sample_certificate=certificate,
                                             prospectus=prospectus,
                                             )
        country_obj=country
        for i in country_obj:
            countries=Country.objects.get(id=i)
        university_obj=university.country.add(countries)
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Successfully added"
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
def view_university(request):
    if (university:=University.objects.filter(is_deleted=False)).exists():
        serialized_data=UniversitySerializer(university,
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
@group_required(['ezgrad_admin'])
def edit_university(request,pk):
    logo=request.data.get('university_logo')
    name=request.data.get('university_name')
    about=request.data.get('about_university')
    certificate=request.data.get('sample_certificate')
    prospectus=request.data.get('prospectus')
    country=request.data.get('country')
    if (u:=University.objects.filter(pk=pk,is_deleted=False)).exists():
        university=u.latest('id')
        if logo:
            university.university_logo=logo
        if name:
            university.university_name=name
        if about:
            university.about_university=about
        if certificate:
            university.sample_certificate=certificate
        if prospectus:
            university.prospectus=prospectus
        if country:
            university.country=country
        university.save()
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
def delete_university(request,pk):
    if (u:=University.objects.filter(pk=pk,is_deleted=False)).exists():
        university=u.latest('id')
        university.is_deleted=True
        university.save()
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
def list_universitylogo_studentform(request):
    country=request.data.getlist('country')
    if (university:=University.objects.filter(country__in=country)).exists():
        serialized_data=UniversitySerializer(university,
                                             context={
                                                 "request":request,
                                             },
                                             many=True,).data
        university_count=University.objects.filter(country__in=country).count()
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
    return Response({'app_data':response_data,"count":university_count})


@api_view(['GET'])
def list_course_studentform(request):
    course=request.data.get('course')
    country=request.data.get('country')
    if course and country:
        courses = Course.objects.filter(course_name=course, university__country__in=country)
        if courses.exists():
            serialized_data = CourseSerializer(courses, context={"request": request}, many=True).data
            response_data = {
                "StatusCode": 6000,
                "data": serialized_data
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


@api_view(['GET'])
def list_popular_university(request):
    service=request.data.get('service')
    coursetype=request.data.get('coursetype')
    country=request.data.get('country')
    if (coursetypes:=CourseType.objects.get(id=coursetype,service=service,is_deleted=False)):
        service=ServiceType.objects.filter(id=service)
        services=service.latest('id')
        service_name=services.service
        if (university:=University.objects.filter(coursetype=coursetypes,country=country,is_deleted=False)).exists():
            serialized_data=UniversitySerializer(university,
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
    else:
         response_data={
                "StatusCode":6001,
                "data":{
                    "title":"Failed",
                    "Message":"Not Found"
                }
            }

    return Response({'app_data':response_data,"service":service_name})



@api_view(['POST'])
@group_required(['ezgrad_admin'])
def add_facts(request):
    serialized_data=FactSerializer(data=request.data)
    if serialized_data.is_valid():
        facts=request.data['facts']
        university=request.data['university']
        if (u:=University.objects.filter(id=university,is_deleted=False)).exists():
            u=u.latest('id')
            fact=Facts.objects.create(university=u,
                                      facts=facts)
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
def view_facts(request):
    if (fact:=Facts.objects.filter(is_deleted=False)).exists():
        serialized_data=FactSerializer(fact,
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
@group_required(['ezgrad_admin'])
def edit_facts(request,id):
    facts=request.data.get('facts')
    if (fact:=Facts.objects.filter(id=id,is_deleted=False)).exists():
        fact=fact.latest('id')
        if facts:
            fact.facts=facts
        fact.save()
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
def delete_facts(request,id):
    if (fact:=Facts.objects.filter(id=id,is_deleted=False)).exists():
        fact=fact.latest('id')
        fact.is_deleted=True
        fact.save()
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
@group_required(['ezgrad_admin'])
def add_approval(request):
    serialized_data=ApprovalSerializer(data=request.data)
    if serialized_data.is_valid():
        university=request.data['university']
        approved_by=request.data['approved_by']
        logo=request.data['logo']
        if (u:=University.objects.filter(id=university,is_deleted=False)).exists():
            u=u.latest('id')
            approval=Approval.objects.create(university=u,
                                             approved_by=approved_by,
                                             logo=logo)
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
def view_approval(request):
    if (approval:=Approval.objects.filter(is_deleted=False)).exists():
        serialized_data=ApprovalSerializer(approval,
                                           context={
                                               "request":request,
                                           },
                                           many=True).data
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
@group_required(['ezgrad_admin'])
def edit_approval(request,id):
    approved_by=request.data.get('approved_by')
    logo=request.data.get('logo')
    if (approval:=Approval.objects.filter(id=id,is_deleted=False)).exists():
        approval=approval.latest('id')
        if approved_by:
            approval.approved_by=approved_by
        if logo:
            approval.logo=logo
        approval.save()
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
def delete_approval(request,id):
    if (approval:=Approval.objects.filter(id=id,is_deleted=False)).exists():
        approval=approval.latest('id')
        approval.is_deleted=True
        approval.save()
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
def university_list(request):
    service=request.data.get('service')
    coursetype=request.data.get('coursetype')
    if (coursetype:=CourseType.objects.filter(id=coursetype,service=service,is_deleted=False)).exists():
            coursetypes=coursetype.latest('id')
            if (university:=University.objects.filter(coursetype=coursetypes,is_deleted=False)).exists():
                serialized_data=UniversitySerializer(university,
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
                        "Message":"Universities Not Found"
                    }
                }
    else:
            response_data={
                "StatusCode":6001,
                "data":
                {
                    "title":"Failed",
                    "Message":"Coursetype Not Found"
                }
            }
    return Response({'app_data':response_data})


@api_view(['GET'])
def fact_list(request):
    university=request.data.get('university')
    if (facts:=Facts.objects.filter(university=university,is_deleted=False)).exists():
        serialized_data=FactSerializer(facts,
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


@api_view(['GET'])    
def approval_list(request):
    university=request.data.get('university')
    if (approval:=Approval.objects.filter(university=university,is_deleted=False)).exists():
        serialized_data=ApprovalSerializer(approval,
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
                "title":"Success",
                "data":"Not Found"
            }
        }
    return Response({'app_data':response_data})
        
@api_view(['GET'])
def list_university_logo(request):
    if (university:=University.objects.filter(is_deleted=False)).exists():
        serialized_data=UniversitySerializer(university,
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

        
@api_view(['POST'])
@group_required(['ezgrad_admin'])
def add_course(request):
    serialized_data=CourseSerializer(data=request.data)
    if serialized_data.is_valid():
        university=request.data['university']
        course_type=request.data['coursetype']
        course_name=request.data['course_name']
        icon=request.data['icon']
        duration=request.data['duration']
        duration_description=request.data['duration_description']
        course_image=request.data['course_image']
        course_details=request.data['course_details']
        video=request.data['video']
        audio=request.data['audio']
        eligibility=request.data['eligibility']
        eligibility_description=request.data['eligibility_description']
        admission_procedure=request.data['admission_procedure']
        fees=request.data['fees']
        fees_description=request.data['fees_description']
        syllabus=request.data['syllabus']

        if (u:=University.objects.filter(coursetype=course_type,id=university,is_deleted=False)).exists():
            u=u.latest('id')
            course=Course.objects.create(university=u,
                                         course_name=course_name,
                                         icon=icon,
                                         duration=duration,
                                         duration_description=duration_description,
                                         course_image=course_image,
                                         course_details=course_details,
                                         video=video,
                                         audio=audio,
                                         eligibility=eligibility,
                                         eligibility_description=eligibility_description,
                                         admission_procedure=admission_procedure,
                                         fees=fees,
                                         fees_description=fees_description,
                                         syllabus=syllabus)
            response_data={
                "StatusCode":6000,
                "data":{
                    "title":"Success",
                    "Message":"Successfully added"
                }
            }
        else:
            response_data={
                "data":{
                    "title":"Failed",
                    "Message":"Not Found"
                }
            }
    else:
            response_data={
                "StatusCode":6001,
                "data":
                {
                    "title":"Failed",
                    "Message":generate_serializer_errors(serialized_data._errors)
                }
            }
    return Response({'app_data':response_data})


@api_view(['GET'])
@group_required(['ezgrad_admin'])
def view_course(request):
    if (course:=Course.objects.filter(is_deleted=False)).exists():
        serialized_data=CourseSerializer(course,
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
@group_required(['ezgrad_admin'])
def edit_course(request,pk):
    course_name=request.data.get('course_name')
    icon=request.data.get('icon')
    duration=request.data.get('duration')
    duration_description=request.data.get('duration_description')
    course_image=request.data.get('course_image')
    course_details=request.data.get('course_details')
    video=request.data.get('video')
    audio=request.data.get('audio')
    eligibility=request.data.get('eligibility')
    eligibility_description=request.data.get('eligibility_description')
    admission_procedure=request.data.get('admission_procedure')
    fees=request.data.get('fees')
    fees_description=request.data.get('fees_description')
    syllabus=request.data.get('syllabus')
    if (course:=Course.objects.filter(pk=pk,is_deleted=False)).exists():
        course=course.latest('id')
        if course_name:
            course.course_name=course_name
        if icon:
            course.icon=icon
        if duration:
            course.duration=duration
        if duration_description:
            course.duration_description=duration_description
        if course_image:
            course.course_image=course_image
        if course_details:
            course.course_details=course_details
        if video:
            course.video=video
        if audio:
            course.audio=audio
        if eligibility:
            course.eligibility=eligibility
        if eligibility_description:
            course.eligibility_description=eligibility_description
        if admission_procedure:
            course.admission_procedure=admission_procedure
        if fees:
            course.fees=fees
        if fees_description:
            course.fees_description=fees_description
        if syllabus:
            course.syllabus=syllabus
        course.save()
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
def delete_course(request,pk):
    if (course:=Course.objects.filter(pk=pk,is_deleted=False)).exists():
        course=course.latest('id')
        course.is_deleted=True
        course.save()
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
@group_required(['ezgrad_admin'])
def add_specialization(request):
    serialized_data=CourseSpecializationSerializer(data=request.data)
    if serialized_data.is_valid():
        specialization=request.data['specialization']
        course=request.data.get('course')
        if (course_data:=Course.objects.filter(id=course,is_deleted=False)).exists():
            c=course_data.latest('id')
            course_specialization=CourseSpecialization.objects.create(course=c,
                                                                      specialization=specialization)
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
                    "Message":"Not Found"
                }
            }
        return Response({'app_data':response_data})

@api_view(['GET'])
@group_required(['ezgrad_admin'])
def view_specialization(request):
    if (specialization:=CourseSpecialization.objects.filter(is_deleted=False)).exists():
        serialized_data=CourseSpecializationSerializer(specialization,
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
@group_required(['ezgrad_admin'])
def edit_specialization(request,id):
    specialization=request.data.get('specialization')
    if (course_specialization:=CourseSpecialization.objects.filter(id=id,is_deleted=False)).exists():
        c=course_specialization.latest('id')
        if specialization:
            c.specialization=specialization
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
def delete_specialization(request,id):
    if (specialization:=CourseSpecialization.objects.filter(id=id,is_deleted=False)).exists():
        s=specialization.latest('id')
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
def list_specialization(request,pk):
    if (specialization:=CourseSpecialization.objects.filter(course=pk,is_deleted=False)).exists():
        serialized_data=CourseSpecializationSerializer(specialization,
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



@api_view(['GET'])
def list_courses(request):
    service=request.data.get('service')
    coursetype=request.data.get('coursetype')
    if (coursetypes:=CourseType.objects.filter(id=coursetype,service=service,is_deleted=False)).exists():
        if (course:=Course.objects.filter(university__coursetype_id=coursetype,is_deleted=False)).exists():
            if (distinct_course:=course.distinct('course_name')):
                serialized_data=CourseviewSerializer(distinct_course,
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
def add_country(request):
    serialized_data=CountrySerializer(data=request.data)
    if serialized_data.is_valid():
        country=request.data['country']
        flag=request.data['flag']
        c=Country.objects.create(country=country,flag=flag)
        response_data={
            "StatusCode":6000,
            "data":{
                "title":"Success",
                "Message":"Added Successfully",
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
def view_country(request):
    if (country:=Country.objects.filter(is_deleted=False)).exists():
        serialized_data=CountrySerializer(country,
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
@group_required(['ezgrad_admin'])
def edit_country(request,id):
    country=request.data.get('country')
    flag=request.data.get('flag')
    if (c:=Country.objects.filter(id=id,is_deleted=False)).exists():
        c=c.latest('id')
        if country:
            c.country=country
        if flag:
            c.flag=flag
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
def delete_country(request,id):
    if (country:=Country.objects.filter(id=id,is_deleted=False)).exists():
        c=country.latest('id')
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


@api_view(['POST'])
@group_required(['ezgrad-admin'])
def add_faq(request):
    serialized_data=FaqSerializer(data=request.data)
    if serialized_data.is_valid():
        course=request.data['course']
        if (c:=Course.objects.filter(id=course,is_deleted=False)).exists():
            course_id=c.latest('id')
            faq_question=request.data['faq_question']
            faq_answer=request.data['faq_answer']
        faq=Faq.objects.create(course=course_id,faq_question=faq_question,
                               faq_answer=faq_answer)
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
def view_faq(request):
    if (faq:=Faq.objects.filter(is_deleted=False)).exists():
        serialized_data=FaqSerializer(faq,
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
            "data":{
                "title":"Failed",
                "Message":"Not Found"
            }
        }
    return Response({'app_data':response_data})

@api_view(['PUT'])
@group_required(['ezgrad-admin'])
def edit_faq(request,id):
        faq_question=request.data.get('faq_question')
        faq_answer=request.data.get('faq_answer')
        if (faq:=Faq.objects.filter(id=id,is_deleted=False)).exists():
            f=faq.latest('id')
            if faq_question:
                f.faq_question=faq_question
            if faq_answer:
                f.faq_answer=faq_answer
            f.save()
            response_data={
                "StatusCode":6000,
                "data":{
                    "title":"Success",
                    "Message":"Updated Successfully"
                }
            }
        else:
            response_data={
                "StatusCode":6000,
                "data":{
                    "title":"Failed",
                    "Message":"Not Found"
                }
            }
        return Response({'app_data':response_data})

@api_view(['DELETE'])
@group_required(['ezgrad_admin'])
def delete_faq(request,id):
    if (faq:=Faq.objects.filter(id=id,is_deleted=False)).exists():
        f=faq.latest('id')
        f.is_deleted=True
        f.save()
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
def list_faq(request,pk):
    if (faq:=Faq.objects.filter(course=pk,is_deleted=False)).exists():
        serialized_data=FaqSerializer(faq,
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


        















   
            
                             





    




        









        







        

        
        
















    
      

