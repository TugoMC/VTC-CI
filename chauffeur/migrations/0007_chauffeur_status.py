# Generated by Django 4.2 on 2024-09-16 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chauffeur', '0006_alter_historiquelicenciement_chauffeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='chauffeur',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('terminated', 'Terminated')], default='active', max_length=10),
        ),
    ]
