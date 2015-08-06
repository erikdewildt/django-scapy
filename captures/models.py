import uuid

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

capture_files_storage = FileSystemStorage(location=settings.MEDIA_ROOT+'captures')

def get_capture_file_path(instance, filename):
    """
    Generate random filename path
    :param instance:
    :param filename: original filename
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename


class Capture(models.Model):
    """
    A Capture of network traffic
    """
    name = models.CharField(max_length=64, blank=False)
    filename = models.CharField(max_length=64, blank=False)
    file_size = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=get_capture_file_path, storage=capture_files_storage)

    def save(self, *args, **kwargs):
        # Set filename only after upload
        if self.filename == '':
            self.filename = self.file.name
        self.file_size = self.file.size
        super(Capture, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Capture)
def capture_delete(sender, instance, **kwargs):
    """
    Called when instance of Capture is deleted to remove file from filesystem
    """
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)