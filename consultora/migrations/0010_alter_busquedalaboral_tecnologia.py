# Generated by Django 4.1.2 on 2022-10-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultora', '0009_busquedalaboral_tecnologia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busquedalaboral',
            name='tecnologia',
            field=models.ManyToManyField(to='consultora.tecnologia'),
        ),
    ]