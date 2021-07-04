from django.db import models

# Create your models here.

class Planning(models.Model):
	id_student= models.IntegerField()
	id_instructor= models.IntegerField()
	date= models.CharField(max_length=100)
	lieu= models.CharField(max_length=100)
	heure= models.CharField(max_length=100)