import os
import uuid

from django.db import models


def get_capture_file_path(instance, filename):
    """
    Generate random filename path
    :param instance:
    :param filename: original filename
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('captures', filename)


class Capture(models.Model):
    """
    A Capture of network traffic
    """
    name = models.CharField(max_length=64, blank=False)
    filename = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=get_capture_file_path)

    def __str__(self):
        return self.name
