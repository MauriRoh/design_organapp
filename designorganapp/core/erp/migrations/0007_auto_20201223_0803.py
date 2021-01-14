# Generated by Django 3.1.4 on 2020-12-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_detsale_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO'), ('O', 'OTRO')], default='O', max_length=1, verbose_name='Género'),
        ),
    ]
