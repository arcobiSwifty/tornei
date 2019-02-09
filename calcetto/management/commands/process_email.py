from django.core.management.base import BaseCommand, CommandError
from calcetto.models import *
from datetime import datetime, timezone, timedelta
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Sends emails to each team\'s contact 2 days before a game. Y E E T'

    def add_arguments(self, parser):
        parser.add_argument('--id')

    def handle(self, *args, **options):
        utc_dt = datetime.now(timezone.utc) # UTC time
        dt = utc_dt.astimezone()
        email_date = dt + timedelta(days=3)
        for partita in Partita.objects.filter(finita=False, email_sent=False):
            if partita.data < email_date:
                self.sendemail(partita, [partita.squadra_1.contatto, partita.squadra_2.contatto])
                partita.email_sent = True
                partita.save()

    def sendemail(self, partita, destinatari):
        send_mail(subject="Tornei scolastici di calcetto",
                  message="Vi ricordiamo che la partita si svolgerà il {}/{} alle ore {}:{}. Hai ricevuto questa mail perchè sei stato indicato come contatto della tua squadra.".format(partita.data.day, partita..data.month, partita.data.hour, partita.data.minute),
                  from_email='torneigalileogalilei@gmail.com',
                  recipient_list=destinatari)
