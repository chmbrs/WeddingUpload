from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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

# def home(request):
#     articles = Article.objects.all().prefetch_related('likes')
#     for a in articles:
#         a.is_liked = (request.user in a.likes.all())
#
#     return render(request, 'home.html', {'articles': articles})
