from django.contrib import messages
from django.db.models import Sum
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from scapy.all import *

from .forms import CaptureForm
from .models import Capture, capture_files_storage


class CaptureCreate(CreateView):
    """
    View for uploading new capture files
    """
    model = Capture
    form_class = CaptureForm
    success_url = reverse_lazy('captures:capture-list')

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.filename = self.object.file.name
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


class CaptureList(ListView):
    """
    View for the list of uploaded captures.
    """
    model = Capture
    context_object_name = 'captures'

    def get_context_data(self, **kwargs):
        context = super(CaptureList, self).get_context_data(**kwargs)
        context['number_of_files'] = Capture.objects.count()
        context['total_size'] = Capture.objects.aggregate(Sum('file_size'))
        return context


class CaptureDelete(DeleteView):
    """
    Remove capture file
    """
    model = Capture
    success_url = reverse_lazy('captures:capture-list')


class CaptureEdit(UpdateView):
    """
    Update the capture file name and/or description
    """
    model = Capture
    success_url = reverse_lazy('captures:capture-list')
    fields = ['name', 'description']


class CaptureDetail(DetailView):
    """
    Show Capture file details
    """
    model = Capture
    allow_empty = True
    context_object_name = 'capture'

    def get_context_data(self, **kwargs):
        context = super(CaptureDetail, self).get_context_data(**kwargs)
        file = capture_files_storage.base_location + "/" + str(self.object.file)
        packets = rdpcap(capture_files_storage.base_location + "/" + str(self.object.file))
        context['number_of_packets'] = len(packets)
        packet_list = []
        for pkt in packets:
            packet_list.append(pkt.show())

        context['packets_list'] = packet_list
        return context

    def get(self, request, *args, **kwargs):
        """
        Redirect to list page if no object is found
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self.object = self.get_object()
            # Register capture_id and capture_name in session
            request.session['capture_id'] = self.object.id
            request.session['capture_name'] = self.object.name
        except Http404:
            request.session['capture_id'] = 0
            request.session['capture_name'] = ''
            # redirect here
            messages.add_message(request, messages.ERROR, 'No valid capture file selected. Please select a capture file.')
            url = reverse_lazy('captures:capture-list')
            return redirect(url)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


