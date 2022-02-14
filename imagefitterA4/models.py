from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class ImageResource(models.Model):
    source = models.ImageField(upload_to=settings.IMAGE_URL,
                               validators=[FileExtensionValidator(['jpeg', 'jpg'])])
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    orientation = models.CharField(max_length=20)