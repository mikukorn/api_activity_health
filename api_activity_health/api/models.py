from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.height and self.weight:
            # Вычисление ИМТ
            self.bmi = self.weight / (self.height ** 2)
        else:
            self.bmi = None
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    TYPE_CHOICES = (
        ('measure', 'Замеры'),
        ('calories_plus', 'Питание'),
        ('calories_minus', 'Упражнение/активность'),
        ('summary', 'Заметка'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    value = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag, through='TagActivity')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class TagActivity(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} {self.activity}'


class DaySummary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    total_food = models.PositiveIntegerField(default=0)
    total_calories = models.PositiveIntegerField(default=0)
    total_summary = models.PositiveIntegerField(default=0)
