# Generated by Django 2.1.4 on 2019-02-06 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartellino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ammonizione', 'Ammonizione'), ('cartellino_rosso', 'Cartellino Rosso'), ('cartillino_giallo', 'Cartellino Giallo')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizzato', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniziata_il', models.DateTimeField(blank=True, null=True)),
                ('finita_il', models.DateTimeField(blank=True, null=True)),
                ('result', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('finita', models.BooleanField(default=False)),
                ('goals', models.ManyToManyField(to='calcetto.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Squadra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.CharField(max_length=30)),
                ('score', models.IntegerField(default=0)),
                ('eliminata', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Studente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cartellini', models.ManyToManyField(to='calcetto.Cartellino')),
            ],
        ),
        migrations.AddField(
            model_name='squadra',
            name='calciatori',
            field=models.ManyToManyField(to='calcetto.Studente'),
        ),
        migrations.AddField(
            model_name='partita',
            name='squadra_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squadra_1', to='calcetto.Squadra'),
        ),
        migrations.AddField(
            model_name='partita',
            name='squadra_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squadra_2', to='calcetto.Squadra'),
        ),
        migrations.AddField(
            model_name='goal',
            name='giocatore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calcetto.Studente'),
        ),
        migrations.AddField(
            model_name='goal',
            name='squadra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calcetto.Squadra'),
        ),
        migrations.AddField(
            model_name='cartellino',
            name='partita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calcetto.Partita'),
        ),
    ]
