from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

class Content(models.Model):
    thumbnail = models.TextField(blank=False)
    shortthumb = models.TextField(blank=False,default="null")
    country = models.CharField(blank = False, max_length = 200, default= "India")
    heading = models.TextField(blank=False,default="null")
    subhead = models.TextField(blank=True)
    img = CloudinaryField('image')
    cont=models.TextField(blank=False)
    Date = models.DateTimeField(default=datetime.now, blank=True)
    is_published=models.BooleanField(default=True)
    def __str__(self):
        return self.thumbnail