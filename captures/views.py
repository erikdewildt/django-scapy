from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import CaptureForm
from .models import Capture


class CaptureCreate(CreateView):
    """
    View for uploading new capture files
    """
    model = Capture
    form_class = CaptureForm
    success_url = reverse_lazy('captures:capture-list')


class CaptureList(ListView):
    model = Capture
    context_object_name = 'captures'

