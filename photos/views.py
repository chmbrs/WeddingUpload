from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic.base import RedirectView

from django.shortcuts import get_object_or_404

from upload.models import Photo

class DocumentCreateView(CreateView):
    model = Photo
    fields = ['upload', ]
    success_url = reverse_lazy('upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = Photo.objects.all()
        context['photos'] = photos
        return context

class LikePhotoToogle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        photo = get_object_or_404(Photo, slug=slug)

        user = self.request.user
        if user.is_authenticated:
            if user in photo.likes.all():
                photo.likes.remove(user)
            else:
                photo.likes.add(user)

        return reverse_lazy('photos:canvas')
