from django.db import models
from general.models import BaseModel

class University(BaseModel):
    coursetype=models.ForeignKey('services.CourseType',on_delete=models.CASCADE,blank=True,null=True)
    country=models.ManyToManyField('Country')
    university_logo=models.ImageField(upload_to='Images',blank=True,null=True)
    university_name=models.CharField(max_length=300,blank=True,null=True)
    about_university=models.TextField(blank=True,null=True)
    sample_certificate=models.ImageField(upload_to='Images',blank=True,null=True)
    prospectus=models.FileField(upload_to='Files',blank=True,null=True)
    class Meta:
        db_table='University'
    
    def __str__(self):
        return self.university_name


class Facts(models.Model):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    facts=models.TextField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Facts'
    def __str__(self):
        return self.facts


class Approval(models.Model):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    approved_by=models.CharField(max_length=200,blank=True,null=True)
    logo=models.ImageField(upload_to='Images',blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Approval'

    def __str__(self):
        return self.approved_by

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
    
    def __str__(self):
        return self.course_name

class CourseSpecialization(models.Model):
    course=models.ForeignKey('course.Course',on_delete=models.CASCADE,blank=True,null=True)
    specialization=models.CharField(max_length=300,blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='CourseSpecialization'
    
    def __str__(self):
        return self.specialization

class Country(models.Model):
    country=models.CharField(max_length=200,blank=True,null=True)
    flag=models.ImageField(upload_to='Images',blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Country'
    
    def __str__(self):
        return self.country

class Faq(models.Model):
    course=models.ForeignKey('course.Course',on_delete=models.CASCADE,blank=True,null=True)
    faq_question=models.TextField(blank=True,null=True)
    faq_answer=models.TextField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Faq'
    
    def __str__(self):
        return self.faq_question

class FoodFacility(models.Model):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    photo=models.ImageField(upload_to='Images',blank=True,null=True)
    fees=models.IntegerField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='FoodFacility'

    def __str__(self):
        return self.name

class Hostel(models.Model):
    university=models.ForeignKey('course.University',on_delete=models.CASCADE,blank=True,null=True)
    hostel_name=models.CharField(max_length=200,blank=True,null=True)
    hostel_image=models.ImageField(upload_to='Images',blank=True,null=True)
    distance=models.CharField(max_length=200,blank=True,null=True)
    fees=models.IntegerField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Hostel'

    def __str__(self):
        return self.hostel_name


    
# Create your models here.
