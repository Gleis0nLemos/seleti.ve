# Generated by Django 4.1.3 on 2022-11-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=60)),
                ('caracteristica_empresa', models.TextField()),
            ],
        ),
    ]
