# Generated by Django 4.0.4 on 2022-12-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_business_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_news',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='health_news',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='science_news',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='sport_news',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='tech_news',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
