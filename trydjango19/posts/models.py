from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
	title= models.CharField(max_length=200 )
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.title
# Create your models here.
