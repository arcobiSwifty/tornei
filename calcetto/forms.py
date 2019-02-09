from django import forms
from .models import *

class CreaGoal(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('minuto', 'giocatore')
        labels = {
            'minuto': 'realizzato al minuto',
            'giocatore': 'realizzato da'
        }

class CreaPartita(forms.ModelForm):
    data = forms.DateField(required=True, input_formats=['%d-%m-%Y %H:%M', '%d/%m/%Y %H:%M'])
    class Meta:
        model = Partita
        fields = ('squadra_1', 'squadra_2')
        labels = {
            'squadra_1': 'prima squadra',
            'squadra_2': 'seconda squadra',
            'data': 'data',
        }
