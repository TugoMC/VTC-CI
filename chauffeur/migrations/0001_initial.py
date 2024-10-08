# Generated by Django 4.2 on 2024-09-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('numero_piece', models.CharField(max_length=100, unique=True)),
                ('lieu_de_residence', models.CharField(max_length=255)),
                ('nom_pere', models.CharField(max_length=100)),
                ('nom_mere', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='chauffeurs_photos/')),
            ],
        ),
    ]
