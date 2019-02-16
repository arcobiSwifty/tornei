from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('pallavolo', views.ListPartite.as_view()),
]
