# Generated by Django 4.2 on 2024-09-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chauffeur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chauffeur',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='chauffeur',
            name='numero_piece',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chauffeur',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='chauffeur_photos/'),
        ),
    ]
