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
        widgets = {
            'minuto': forms.NumberInput(attrs={'placeholder': 'Inserisci il minuto'})
        }

class CreaPartita(forms.ModelForm):
    data = forms.DateTimeField(required=True, input_formats=['%d-%m-%Y %H:%M', '%d/%m/%Y %H:%M'])
    class Meta:
        model = Partita
        fields = ('squadra_1', 'squadra_2')
        labels = {
            'squadra_1': 'prima squadra',
            'squadra_2': 'seconda squadra',
            'data': 'data',
        }

class CreaSquadra(forms.ModelForm):
    studente_1 = forms.CharField(max_length=100, strip=True)
    studente_2 = forms.CharField(max_length=100, strip=True)
    studente_3 = forms.CharField(max_length=100, strip=True)
    studente_4 = forms.CharField(max_length=100, strip=True)
    studente_5 = forms.CharField(max_length=100, strip=True)
    studente_6 = forms.CharField(max_length=100, strip=True, required=False)
    studente_7 = forms.CharField(max_length=100, strip=True, required=False)
    studente_8 = forms.CharField(max_length=100, strip=True, required=False)
    studente_9 = forms.CharField(max_length=100, strip=True, required=False)
    studente_10 = forms.CharField(max_length=100, strip=True, required=False)
    class Meta:
        model = Squadra
        fields = ('classe', 'contatto')
        labels = {
            'studente_1': 'aggiungi giocatore',
            'studente_2': 'aggiungi giocatore',
            'studente_3': 'aggiungi giocatore',
            'studente_4': 'aggiungi giocatore',
            'studente_5': 'aggiungi giocatore',
            'studente_6': 'aggiungi giocatore',
            'studente_7': 'aggiungi giocatore',
            'studente_8': 'aggiungi giocatore',
            'studente_9': 'aggiungi giocatore',
            'studente_10': 'aggiungi giocatore',
        }

class CreaCartellino(forms.ModelForm):
    class Meta:
        model = Cartellino
        fields = ('tipo',)
        labels = {'tipo': 'Seleziona il tipo di cartellino'}
        forms.TextInput(attrs={'placeholder': 'Inserisci il titolo...'})
