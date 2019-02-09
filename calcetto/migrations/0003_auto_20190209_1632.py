# Generated by Django 2.1.4 on 2019-02-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcetto', '0002_goal_minuto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partita',
            name='finita_il',
        ),
        migrations.AddField(
            model_name='partita',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squadra',
            name='contatto',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='partita',
            name='data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='partita',
            name='result',
            field=models.CharField(blank=True, default='0-0', max_length=10, null=True),
        ),
    ]