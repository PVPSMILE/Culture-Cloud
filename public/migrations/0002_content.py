# Generated by Django 4.0.4 on 2022-07-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('poster', models.ImageField(upload_to='main/', verbose_name='Poster')),
            ],
        ),
    ]
