# Generated by Django 4.0.4 on 2022-12-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('Business', 'Business'), ('Health', 'Health'), ('Tech', 'Tech'), ('Sport', 'Sport'), ('Science', 'Science')], max_length=200, null=True),
        ),
    ]
