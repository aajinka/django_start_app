# Generated by Django 3.1.7 on 2021-02-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
    ]
