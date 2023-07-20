from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 
    class Meta:
        abstract = True

class Register(BaseModel):

    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    mobile=models.BigIntegerField(blank=True,null=True)
    gender=models.CharField(max_length=100,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    country=models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        db_table="Register"
        ordering=('id',)

    def __str__(self):
        return str(self.id)
# Create your models here.
