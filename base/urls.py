from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
         path ('', views.home,name="home"),
         path('room/<str:pk>/',views.room,name = "room"),
         path('profile/',views.ProfileView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)