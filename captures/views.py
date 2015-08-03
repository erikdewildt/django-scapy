from django.http import HttpResponseRedirect
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.filename = self.object.file.name
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CaptureList(ListView):
    """
    View for the list of uploaded captures.
    """
    model = Capture
    context_object_name = 'captures'

