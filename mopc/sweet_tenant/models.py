from django.db import models
from sweet_shared.models import SweetType

class Sweet(models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete = models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
