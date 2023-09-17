from django.db import models

class Upload(models.Model):
    """Model definition for Upload."""

    caption = models.CharField (max_length=100)
    image = models.ImageField(upload_to="images/")

    class Meta:
        """Meta definition for Upload."""

        verbose_name =  'Upload'
        verbose_name_plural =  'Uploads'

    def __str__(self):
        return self.caption

