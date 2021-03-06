# Generated by Django 4.0.2 on 2022-02-18 20:00

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('photo', models.ImageField(upload_to=main_page.models.Gallery.get_file_name)),
            ],
        ),
    ]
