from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', views.Main.as_view()),
    path('calcetto', views.ListPartite.as_view()),
    path('calcetto/classifica', views.Classifica.as_view()),
    path('calcetto/studente/<int:pk>', views.StudenteDetail.as_view()),
    path('accounts/login/',  auth_views.LoginView.as_view()),
    path('accounts/login',  auth_views.LoginView.as_view()),
    path('calcetto/squadre',  views.ListSquadre.as_view()),
    path('calcetto/studente/cartellino/<int:pk>', views.AggiungiCartellino.as_view()),
    path('calcetto/squadra/<int:pk>',  views.DetailSquadra.as_view()),
    path('calcetto/nuovasquadra/', staff_member_required(views.CreateSquadra.as_view())),
    path('calcetto/nuovapartita/', staff_member_required(views.CreatePartita.as_view())),
    path('calcetto/elimina/<int:pk>/p', views.DeleteGoal.as_view()),
    path('calcetto/modifica/<int:pk>/p', views.EditGoal.as_view()),
    path('accounts/logout', auth_views.LogoutView.as_view()),
    path('calcetto/dettagli/<int:pk>', views.DetailPartite.as_view()),
    path('calcetto/arbitra/<int:pk>', login_required(views.ArbitraPartite.as_view())),
    path('calcetto/finisci/<int:pk>', login_required(views.FinisciPartita.as_view())),
]
