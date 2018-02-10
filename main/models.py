from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse


class Encuesta(models.Model):
	CHOICES=[('1','2'),
   	         ('2','4'),
   	         ('3','6'),
   	         ('4','8'),
   	         ('5','10')]
	like = MultiSelectField(choices=CHOICES,default=" ")

	CHOICES2=[('6','2'),
   	         ('7','4'),
   	         ('8','6'),
   	         ('9','8'),
   	         ('10','10')]

	design = MultiSelectField(choices=CHOICES2,default=" ")

	more_like = models.CharField(max_length=100, default=" ")

	CHOICES3=[('11','bueno'),
   	         ('12','malo'),
   	         ]

	price = MultiSelectField(choices=CHOICES3,default=" ")

	def __str__(self):
		return 'Encuesta numero {}'.format(self.id)
