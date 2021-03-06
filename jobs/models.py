from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    hyperlink = models.CharField(max_length=100, default='add hyperlink')
    title = models.CharField(max_length=50, default='add title')
