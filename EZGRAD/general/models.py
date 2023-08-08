from django.db import models
import uuid
from django.contrib.auth.models import User,Group


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted=models.BooleanField(default=False)
    
 
    class Meta:
        abstract = True

class StudentProfile(BaseModel):

    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    mobile=models.BigIntegerField(blank=True,null=True)
    gender=models.CharField(max_length=100,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    country=models.CharField(max_length=200,blank=True,null=True)
    
    username = models.CharField(max_length=128, blank=True, null=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE, blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        db_table="StudentProfile"
        ordering=('id',)

    def __str__(self):
        return str(self.id)
    
class ChiefProfile(BaseModel):
    username = models.CharField(max_length=128)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    password = models.TextField(blank=True, null=True)
    class Meta:
        db_table="ChiefProfile"


      






# Create your models here.
