from django.db import models
from django.utils import timezone


class UploadFile(models.Model):
    # Add a file field for the uploaded file
    file = models.FileField(upload_to='uploads/')

    # This field will automatically store the file name when the file is uploaded
    file_name = models.CharField(max_length=255, blank=True)

    # Date fields
    uploaded_at = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically set the file_name field to the name of the uploaded file
        if self.file:
            self.file_name = self.file.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name
