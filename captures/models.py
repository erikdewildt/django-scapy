from django.db import models


class Capture(models.Model):
    """
    A Capture of network traffic
    """
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True)
    file = models.FileField()

    def __str__(self):
        return self.name
