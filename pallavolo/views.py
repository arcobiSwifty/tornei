from django.shortcuts import render
from .models import *
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

class ListPartite(ListView):
    queryset = Partita.objects.order_by('data')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['is_authenticated'] = self.request.user.is_authenticated
        return data
