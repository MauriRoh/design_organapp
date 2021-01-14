# Generated by Django 3.1.4 on 2020-12-16 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_locality_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Departamento / Partido'),
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=30, verbose_name='Apellido')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='O', max_length=10, verbose_name='Género')),
                ('mobile', models.CharField(blank=True, default='0', max_length=20, verbose_name='Móbil')),
                ('phone', models.CharField(blank=True, default='0', max_length=20, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Email')),
                ('address', models.CharField(blank=True, default='', max_length=30, verbose_name='Dirección')),
                ('neighborhood', models.CharField(blank=True, default='', max_length=20, verbose_name='Barrio')),
                ('localities', models.CharField(blank=True, default='', max_length=20, verbose_name='Localidad')),
                ('postal_code', models.CharField(blank=True, default='', max_length=8, verbose_name='Código Postal')),
                ('others', models.TextField(blank=True, default='', verbose_name='Otros')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.locality', verbose_name='Departamento')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.province', verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'clients',
                'ordering': ['-id'],
                'unique_together': {('surname', 'name', 'email')},
            },
        ),
    ]
