from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class PDBFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdb_id = models.CharField(max_length=4)
    entry_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return f'{self.pdb_id}'

