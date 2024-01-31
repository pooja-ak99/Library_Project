from django.db import models

class Booktable(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.title


