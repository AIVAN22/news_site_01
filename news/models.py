from django.db import models

# Create your models here.


def generate_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"static/business_images/{filename}"


def generate_image_filename_01(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"static/health_images/{filename}"


def generate_image_filename_02(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"static/sport_images/{filename}"


def generate_image_filename_03(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"static/tech_images/{filename}"


def generate_image_filename_04(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"static/science_images/{filename}"


class Business_news(models.Model):

    title = models.CharField(max_length=250, null=False)
    content = models.TextField(max_length=10000, null=False)
    time = models.DateTimeField(auto_now_add=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(
        upload_to=generate_image_filename, default="static/business_images/default.jpg"
    )

    def __str__(self):
        return self.title


class Health_news(models.Model):

    title = models.CharField(max_length=250, null=False)
    content = models.TextField(max_length=10000, null=False)
    time = models.DateTimeField(auto_now_add=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(
        upload_to=generate_image_filename_01, default="static/health_images/default.jpg"
    )

    def __str__(self):
        return self.title


class Sport_news(models.Model):

    title = models.CharField(max_length=250, null=False)
    content = models.TextField(max_length=10000, null=False)
    time = models.DateTimeField(auto_now_add=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(
        upload_to=generate_image_filename_02, default="static/sport_images/default.jpg"
    )

    def __str__(self):
        return self.title


class Tech_news(models.Model):

    title = models.CharField(max_length=250, null=False)
    content = models.TextField(max_length=10000, null=False)
    time = models.DateTimeField(auto_now_add=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(
        upload_to=generate_image_filename_03, default="static/tech_images/default.jpg"
    )

    def __str__(self):
        return self.title


class Science_news(models.Model):

    title = models.CharField(max_length=250, null=False)
    content = models.TextField(max_length=10000, null=False)
    time = models.DateTimeField(auto_now_add=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(
        upload_to=generate_image_filename_04,
        default="static/science_images/default.jpg",
    )

    def __str__(self):
        return self.title
