# Generated by Django 4.0.4 on 2022-12-31 14:41

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_business_news_custom_filename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_news',
            name='img',
            field=models.ImageField(default='static/business_images/default.jpg', upload_to=news.models.generate_image_filename),
        ),
        migrations.AlterField(
            model_name='health_news',
            name='img',
            field=models.ImageField(default='static/business_images/default.jpg', upload_to='business_images/'),
        ),
        migrations.AlterField(
            model_name='science_news',
            name='img',
            field=models.ImageField(default='static/business_images/default.jpg', upload_to='business_images/'),
        ),
        migrations.AlterField(
            model_name='sport_news',
            name='img',
            field=models.ImageField(default='static/business_images/default.jpg', upload_to='business_images/'),
        ),
        migrations.AlterField(
            model_name='tech_news',
            name='img',
            field=models.ImageField(default='static/business_images/default.jpg', upload_to='business_images/'),
        ),
    ]
