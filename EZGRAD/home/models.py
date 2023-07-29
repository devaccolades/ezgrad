from django.db import models

class HomeDetails(models.Model):
    main_banner=models.ImageField(upload_to='Images',blank=True,null=True)
    main_banner_url=models.URLField(blank=True,null=True)
    sub_banner=models.ImageField(upload_to='Images',blank=True,null=True)
    sub_banner_url=models.URLField(blank=True,null=True)
    project_logo=models.ImageField(upload_to='Images',blank=True,null=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table='HomeDetails'



class Contact(models.Model):
    logo=models.ImageField(upload_to='Images',blank=True,null=True)
    about=models.TextField(blank=True,null=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    phone=models.BigIntegerField(blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    facebook_url=models.URLField(blank=True,null=True)
    instagram_url=models.URLField(blank=True,null=True)
    youtube_url=models.URLField(blank=True,null=True)
    whatsapp_url=models.URLField(blank=True,null=True) 
    linkedln_url=models.URLField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Contact'

class Details(models.Model):
    heading=models.CharField(max_length=300,blank=True,null=True)
    body=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='Images',blank=True,null=True)
    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Details'

class Experts(models.Model):
    title=models.CharField(max_length=300,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    role=models.CharField(max_length=200,blank=True,null=True)
    experience=models.CharField(max_length=200,blank=True,null=True)
    photo=models.ImageField(upload_to='Images',blank=True,null=True)
    rating=models.IntegerField(blank=True,null=True)
    counselling=models.IntegerField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Experts'













# Create your models here.


# Create your models here.
