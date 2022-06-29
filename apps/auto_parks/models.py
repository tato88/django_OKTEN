from django.db import models


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
