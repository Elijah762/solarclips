# Generated by Django 4.0.4 on 2022-04-24 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_cover'),
        ('social', '0002_rename_reviews_review_delete_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]
