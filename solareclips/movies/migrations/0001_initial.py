# Generated by Django 4.0.4 on 2022-04-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=350)),
                ('esrb', models.CharField(max_length=5)),
                ('cover', models.ImageField(null=True, upload_to='images')),
                ('director', models.CharField(max_length=50)),
                ('starring', models.CharField(max_length=200)),
            ],
        ),
    ]
