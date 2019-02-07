from django.shortcuts import render, redirect

from .models import *
from .forms import CreaGoal

from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

# Create your views here.
class ListPartite(ListView):
    queryset = Partita.objects.all()
    paginate_by = 20

class DetailPartite(DetailView):
    model = Partita
    def get_context_data(self, **kwargs):
        context = super(DetailPartite, self).get_context_data(**kwargs)
        context['goals'] = Partita.objects.get(pk=self.kwargs['pk']).goals.all()
        return context

class EditGoal(UpdateView):
    model = Goal
    fields = ['giocatore', 'minuto', 'squadra']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return '/calcetto/arbitra/{0}'.format(self.request.GET.get('partita'))

class DeleteGoal(UpdateView):
    model = Goal
    def get_success_url(self):
        return '/calcetto/arbitra/{0}'.format(self.request.GET.get('partita'))

class ArbitraPartite(View):
    template_name = 'arbitra.html'
    def get(self, request, pk):
        form = CreaGoal()
        partita = Partita.objects.get(pk=pk)
        squadra1 = partita.squadra_1
        squadra2 = partita.squadra_2
        form.fields["giocatore"].queryset = squadra1.calciatori.all() | squadra2.calciatori.all()
        return render(request, self.template_name, {'partita': partita, 'goals': partita.goals.all(), 'form': form, 'squadra1': squadra1.calciatori.all(), 'squadra2': squadra2.calciatori.all()})
    def post(self, request, pk):
        partita = Partita.objects.get(pk=pk)
        form = CreaGoal(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.squadra = Squadra.objects.get(calciatori__nome=goal.giocatore.nome)
            goal.save()
            partita.goals.add(goal)
            partita.save()
            return redirect('/calcetto/arbitra/{}'.format(pk))
