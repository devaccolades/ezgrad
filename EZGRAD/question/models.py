from django.db import models

class Questions(models.Model):
    question=models.CharField(max_length=500,blank=True,null=True)
    class Meta:
        db_table='Questions'

class Options(models.Model):
    question=models.ForeignKey('question.Questions', on_delete=models.CASCADE, blank=True, null=True)
    options=models.CharField(max_length=300,blank=True,null=True)
    class Meta:
        db_table='Options'

class RecordAnswer(models.Model):
    question=models.ForeignKey('question.Questions', on_delete=models.CASCADE, blank=True, null=True)
    



# Create your models here.

