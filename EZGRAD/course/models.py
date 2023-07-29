from django.db import models
from general.models import BaseModel

class University(BaseModel):
    coursetype=models.ForeignKey('services.CourseType',on_delete=models.CASCADE,blank=True,null=True)
    university_logo=models.ImageField(upload_to='Images',blank=True,null=True)
    university_name=models.CharField(max_length=300,blank=True,null=True)
    about_university=models.TextField(blank=True,null=True)
    sample_certificate=models.ImageField(upload_to='Images',blank=True,null=True)
    prospectus=models.FileField(upload_to='Files',blank=True,null=True)
    country=models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        db_table='University'


class Facts(models.Model):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    facts=models.TextField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Facts'
    

class Approval(models.Model):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    approved_by=models.CharField(max_length=200,blank=True,null=True)
    logo=models.ImageField(upload_to='Images',blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Approval'


class Course(BaseModel):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    course_name=models.CharField(max_length=200,blank=True,null=True)
    icon=models.ImageField(upload_to='Images',blank=True,null=True)
    duration=models.CharField(max_length=200,blank=True,null=True)
    duration_description=models.TextField(blank=True,null=True)
    course_image=models.ImageField(upload_to='Images',blank=True,null=True)
    course_details=models.TextField(blank=True,null=True)
    video=models.FileField(upload_to='Files',blank=True,null=True)
    audio=models.FileField(upload_to='Files',blank=True,null=True)
    eligibility=models.CharField(max_length=200,blank=True,null=True)
    eligibility_description=models.TextField(blank=True,null=True)
    admission_procedure=models.FileField(upload_to='Files',blank=True,null=True)
    fees=models.CharField(max_length=300,blank=True,null=True)
    fees_description=models.TextField(blank=True,null=True)
    syllabus=models.FileField(upload_to='Files',blank=True,null=True)
    class Meta:
        db_table='Course'
        



    
# Create your models here.
