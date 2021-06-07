from django.db import models

# Create your models here.

class LinkCONTAINER(models.Model):
	long_url = models.CharField(max_length=255,null=True,blank=True)
	short_url = models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return f'{self.long_url},{self.short_url}'
