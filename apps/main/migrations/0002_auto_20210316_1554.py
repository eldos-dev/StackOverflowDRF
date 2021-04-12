# Generated by Django 3.1 on 2021-03-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='title_ky',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
