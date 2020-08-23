# Generated by Django 3.1 on 2020-08-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='country',
            field=models.CharField(blank=True, choices=[('Ru', 'Russia'), ('Ukr', 'Ukraine'), ('Ch', 'China')], max_length=100, verbose_name='страна'),
        ),
    ]
