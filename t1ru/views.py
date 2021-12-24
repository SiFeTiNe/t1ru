from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from taggit.models import Tag
from t1ru.models import Announcement


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class AnnouncementView(ListView):
    model = Announcement
    template_name = 'announcement.html'
    context_object_name = 'announcements'
    ordering = ['-pub_date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        object_list = self.model.objects.all().order_by('-pub_date')
        categories = Announcement.CATEGORIES
        announcement_list = {}
        for category in categories:
            announcement_list[category[0]] = []
        for object in object_list:
            announcement_list[object.category].append(object)
        return {self.context_object_name: object_list, 'announcement_list': announcement_list, 'categories': categories}
