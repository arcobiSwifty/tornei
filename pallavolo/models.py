from django.db import models


class Squadra(models.Model):
    classe = models.CharField(max_length=40)
    score = models.IntegerField(default=0)
    contatto = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.classe


class Studente(models.Model):
    nome = models.CharField(max_length=100)
    squadra = models.ForeignKey(Squadra, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' (' + self.squadra.classe + ')'


class Partita(models.Model):
    data = models.DateTimeField('data', blank=True, null=True)
    squadra_1 = models.ForeignKey(Squadra, on_delete=models.CASCADE, related_name="squadra_1")
    squadra_2 = models.ForeignKey(Squadra, on_delete=models.CASCADE, related_name="squadra_2")
    result = models.CharField(default="0-0", blank=True, null=True, max_length=10)
    finita = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.squadra_1.classe + " vs " + self.squadra_2.classe + " " + self.result
