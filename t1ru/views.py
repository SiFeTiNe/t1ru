from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from taggit.models import Tag
from t1ru.models import HomeCarousel


# Create your views here.
class HomeView(ListView):
    model = HomeCarousel
    template_name = 'index.html'
    context_object_name = 'carousels'
