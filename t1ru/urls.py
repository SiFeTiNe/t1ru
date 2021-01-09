from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 't1ru'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('announcement', views.AnnouncementView.as_view(), name='announcement')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
