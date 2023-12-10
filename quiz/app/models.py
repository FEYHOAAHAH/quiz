from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    correct_answer = models.CharField(max_length=255)


class UserAnswer(models.Model):
    user_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
