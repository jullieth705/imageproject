from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class ImageResource(models.Model):
    source = models.ImageField(upload_to=settings.IMAGE_URL, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    orientation = models.CharField(max_length=20, blank=False, null=False)
    dimensions = models.CharField(max_length=20, blank=False, null=False)