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
