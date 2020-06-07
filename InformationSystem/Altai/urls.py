from . import views
from django.urls import path, include

urlpatterns = [
    path('project/<path:id_project>', views.project, name='project'),
    path('initiative', views.initiatives, name='initiative'),
    path('', views.home, name='home-page'),
    path('', include('social_django.urls')),
]
