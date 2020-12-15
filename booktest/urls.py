from django.urls import re_path
from booktest import views
urlpatterns = [
    re_path(r'^heros/$', views.HeroListView.as_view()),
]
