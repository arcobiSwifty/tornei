from django.shortcuts import render, redirect

from .models import *
from .forms import *

from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

#todo implement scheduled tasks
#implement classifica
#implement cartellini e ammonizioni

# Create your views here.
class Main(View):
    def get(self, request):
        return render(request, 'start.html', {'is_staff': self.request.user.is_staff})

class Classifica(ListView):
    queryset = Studente.objects.order_by('-goals')
    paginate_by = 20

class StudenteDetail(DetailView):
    model = Studente
    def get_context_data(self, **kwargs):
        context = super(StudenteDetail, self).get_context_data(**kwargs)
        #non funziona
        context['ammonizioni'] = Studente.objects.get(pk=self.kwargs['pk']).cartellini.all()
        studente = Studente.objects.get(pk=self.kwargs['pk'])
        one = Partita.objects.filter(squadra_1__calciatori=studente).count()
        two = Partita.objects.filter(squadra_2__calciatori=studente).count()
        context['partite_count'] = one + two
        return context

class ListPartite(ListView):
    queryset = Partita.objects.order_by('data')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['is_staff'] = self.request.user.is_staff
        return data

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

    def form_valid(self, form):
        for studente in Studente.objects.all():
            goals = Goal.objects.filter(giocatore=studente).count()
            studente.goals = goals
            studente.save()
        return self.get_success_url()

class DeleteGoal(DeleteView):
    model = Goal
    def get_success_url(self):
        return '/calcetto/arbitra/{0}'.format(self.request.GET.get('partita'))
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        g = self.object.giocatore
        g.goals -= 1
        g.save()
        return super(DeleteGoal, self).delete(*args, **kwargs)

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
            studente = goal.giocatore
            studente.goals += 1
            studente.save()
            if goal.squadra == partita.squadra_1:
                partita.result = "{}-{}".format(int(partita.result[0])+1, partita.result[2])
            elif goal.squadra == partita.squadra_2:
                partita.result = "{}-{}".format(partita.result[0], int(partita.result[2])+1)
            partita.save()
            return redirect('/calcetto/arbitra/{}'.format(pk))

class FinisciPartita(View):
    def get(self, request, pk):
         return render(request, 'calcetto/partita_end.html', {'partita': pk})
    def post(self, request, pk):
        partita = Partita.objects.get(pk=int(pk))
        partita.finita = True
        score = partita.result
        squadra1 = score[0]
        squadra2 = score[2]
        if int(squadra1) > int(squadra2):
            s = Squadra.objects.get(pk=partita.squadra_1.id)
            s.score += 1
            s.save()
        elif int(squadra1) == int(squadra2):
            print("parità")
        elif int(squadra1) < int(squadra2):
            s = Squadra.objects.get(pk=partita.squadra_2.id)
            s.score += 1
            s.save()
        squadra_1_score = 0
        for g in partita.squadra_1.calciatori.all():
            prima = partita.goals.filter(giocatore=g).count()
            squadra_1_score += prima
        squadra_2_score = 0
        for g in partita.squadra_2.calciatori.all():
            prima = partita.goals.filter(giocatore=g).count()
            squadra_2_score += prima
        partita.result = '{}-{}'.format(squadra_1_score, squadra_2_score)


        partita.save()
        return redirect('/calcetto')

class CreatePartita(CreateView):
    template_name = "calcetto/partita_create.html"
    form_class = CreaPartita
    success_url = '/calcetto'
    def form_valid(self, form):
        partita = form.save(commit=False)
        partita.result = "0-0"
        partita.finita = False
        partita.data = form.cleaned_data['data']
        partita.save()
        return super().form_valid(form)
