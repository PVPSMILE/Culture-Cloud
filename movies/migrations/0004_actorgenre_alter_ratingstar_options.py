# Generated by Django 4.0.4 on 2022-07-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_actor_born_actor_end_acting_actor_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='About')),
                ('url', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'ActorGenre',
                'verbose_name_plural': 'ActorGenres',
            },
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Value of rating', 'verbose_name_plural': 'Values of rating'},
        ),
    ]
