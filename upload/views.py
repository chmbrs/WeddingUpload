from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Photos

class DocumentCreateView(CreateView):
    model = Photos
    fields = ['upload', ]
    success_url = reverse_lazy('upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = Photos.objects.all()
        context['photos'] = photos
        return context
