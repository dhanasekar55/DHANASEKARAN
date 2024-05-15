from django.db import models

# Create your models here.
class uv(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=100)
class meta:
    db_table="uv"