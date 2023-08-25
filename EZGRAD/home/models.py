from django.db import models

class HomeDetails(models.Model):
    main_banner=models.ImageField(upload_to='Images',blank=True,null=True)
    main_banner_url=models.URLField(blank=True,null=True)
    status=models.CharField(max_length=128,default="active")
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table='HomeDetails'

    def __str__(self):
        return self.main_banner

class Subbanner(models.Model):
    sub_banner=models.ImageField(upload_to='Images',blank=True,null=True)
    sub_banner_url=models.URLField(blank=True,null=True)
    status=models.CharField(max_length=128,default="active")
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Subbanner'

    def __str__(self):
        return self.sub_banner



class Contact(models.Model):
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
    
    def __str__(self):
        return self.about

class Details(models.Model):
    heading=models.CharField(max_length=300,blank=True,null=True)
    body=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='Images',blank=True,null=True)
    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Details'
    
    def __str__(self):
        return self.heading

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
    
    def __str__(self):
        return self.title













# Create your models here.



