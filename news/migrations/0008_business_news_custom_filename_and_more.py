# Generated by Django 4.0.4 on 2022-12-31 14:34

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_business_news_img_health_news_img_science_news_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_news',
            name='custom_filename',
            field=models.CharField(default='default', max_length=250),
        ),
        migrations.AlterField(
            model_name='business_news',
            name='img',
            field=models.ImageField(default='business_images/default.jpg', upload_to=news.models.generate_image_filename),
        ),
    ]
