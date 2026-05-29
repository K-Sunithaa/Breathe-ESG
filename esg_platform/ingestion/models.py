from django.db import models

# Create your models here.
class RawUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    source_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="UPLOADED")