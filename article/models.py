from django.db import models

# Create your models here.

class Article(models.Model):
	title= models.CharField(max_length=200)
	body= models.TextField()
	date= models.DateTimeField("Publish Date")

	def __unicode__(self):
		return self.title
