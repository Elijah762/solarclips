# Generated by Django 4.0.4 on 2022-04-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(null=True, upload_to='assets'),
        ),
    ]
