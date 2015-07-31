from django import forms

from .models import Capture


class CaptureForm(forms.ModelForm):
    """
    Form for uploading new capture files
    """

    class Meta:
        model = Capture
        fields = ('name', 'description', 'file')
