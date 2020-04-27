from django.db import models

# Create your models here.


class Baby(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(
        'parents.Parent',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.first_name + " " + self.last_name
