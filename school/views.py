from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView)
from school.models import Slideshow,Latestnews,Album,Photos,Staff,Hof
from django.urls import reverse_lazy
from django.utils import timezone


def AboutView(request):
    images = Slideshow.objects.all()
    query = request.GET.get("q")
    if query:
        return render(request, 'school/about.html', {
            'images':images,
        })
    else:
        return render(request, 'school/about.html', {'images': images})

class ReachUs(TemplateView):
    template_name = "reachus.html"
class HOF(ListView):
    model = Hof
    context_object_name = 'hof'
    template_name = "Hall_of_Fame.html"

class Staff(ListView):
    model = Staff
    context_object_name = 'staff'
    template_name = "staff.html"


class LatestnewsListView(ListView):
    model = Latestnews
    context_object_name = 'news_list'
    template_name = 'news_list.html'
    def get_queryset(self):
        return Latestnews.objects.all().order_by('-date')

class LatestnewsDetailView(DetailView):
    model = Latestnews
    context_object_name = 'news_details'
    template_name = 'school/news_detail.html'

class AlbumListView(ListView):
    model=Album
    context_object_name = 'album_list'
    template_name='album_list.html'

class AlbumDetailView(DetailView):
    model=Album
    context_object_name = 'album_details'
    template_name='album_detail.html'
