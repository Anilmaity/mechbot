from django.db import models

# Create your models here.

class Part(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Button(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    value = models.IntegerField()
    max_value = models.IntegerField()
    min_value = models.IntegerField()
    def __str__(self):
        return self.name

class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    value = models.IntegerField()
    max_value = models.IntegerField()
    min_value = models.IntegerField()
    def __str__(self):
        return self.name

class ValueDisplay(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    value = models.IntegerField()
    max_value = models.IntegerField()
    min_value = models.IntegerField()
    def __str__(self):
        return self.name

class Controls(models.Model):
    name = models.CharField(max_length=50)
    buttons = models.ManyToManyField(Button, related_name='buttons')
    slider = models.ManyToManyField(Slider, related_name='slider')
    valuedisplay = models.ManyToManyField(ValueDisplay, related_name='valuedisplay')

    def __str__(self):
        return self.name

class Robot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    year = models.IntegerField()
    serial_number = models.CharField(max_length=50)
    parts = models.ManyToManyField(Part)
    controls = models.ManyToManyField(Controls)
    def __str__(self):
        return self.name