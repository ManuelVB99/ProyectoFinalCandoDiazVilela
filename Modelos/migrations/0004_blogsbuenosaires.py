# Generated by Django 4.1 on 2022-10-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0003_blogsmendoza'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsBuenosAires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('subtitulo', models.CharField(max_length=100)),
                ('cuerpo', models.CharField(max_length=1000)),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogbuenosaires')),
            ],
        ),
    ]