from django.db import models

# Create your models here.

class Person(models.Model):
    class Meta:
        db_table = "person"  # 更改表名
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Animal(models.Model):
    class Meta:
        db_table = "animals"  # 更改表名
        managed = False
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)