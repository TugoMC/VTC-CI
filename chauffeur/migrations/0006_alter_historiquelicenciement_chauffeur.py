# Generated by Django 4.2 on 2024-09-16 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chauffeur', '0005_historiquelicenciement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiquelicenciement',
            name='chauffeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licenciements', to='chauffeur.chauffeur'),
        ),
    ]
