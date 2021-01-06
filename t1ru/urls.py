from django.urls import path

from . import views

app_name = 't1ru'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]