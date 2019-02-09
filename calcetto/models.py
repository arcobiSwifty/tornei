from django.db import models

class Cartellino(models.Model):
    tipi = (
        ('ammonizione', 'Ammonizione'),
        ('cartellino_rosso', 'Cartellino Rosso'),
        ('cartillino_giallo', 'Cartellino Giallo'),
    )
    tipo = models.CharField(max_length=100, choices=tipi)
    partita = models.ForeignKey('Partita', on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

class Studente(models.Model):
    nome = models.CharField(max_length=100)
    cartellini = models.ManyToManyField(Cartellino)

    def __str__(self):
        return self.nome

class Squadra(models.Model):
    classe = models.CharField(max_length=30)
    calciatori = models.ManyToManyField(Studente)
    score = models.IntegerField(default=0)
    eliminata = models.BooleanField(default=False)
    contatto = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.classe

class Goal(models.Model):
    realizzato = models.DateTimeField(auto_now_add=True, blank=True)
    minuto = models.IntegerField()
    giocatore = models.ForeignKey(Studente, on_delete=models.CASCADE)
    squadra = models.ForeignKey(Squadra, on_delete=models.CASCADE)

    def __str__(self):
        return self.giocatore.nome + " (" + str(self.minuto) + "')"

class Partita(models.Model):
    data = models.DateTimeField('data', blank=True, null=True)
    squadra_1 = models.ForeignKey(Squadra, on_delete=models.CASCADE, related_name="squadra_1")
    squadra_2 = models.ForeignKey(Squadra, on_delete=models.CASCADE, related_name="squadra_2")
    goals = models.ManyToManyField(Goal)
    result = models.CharField(default="0-0", blank=True, null=True, max_length=10)
    finita = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.squadra_1.classe + " vs " + self.squadra_2.classe + " " + self.result
