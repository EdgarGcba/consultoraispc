# Generated by Django 3.0 on 2022-10-23 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultora', '0002_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante',
            name='tipodocumento',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultora.Documento'),
        ),
    ]