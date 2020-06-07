from . import views
from django.urls import path, include

urlpatterns = [
    path('project', views.project, name='project'),
    path('', views.home, name='home-page'),
    path('', include('social_django.urls')),
]
