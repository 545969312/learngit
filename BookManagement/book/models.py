from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # 999999.99
    pub_date = models.DateTimeField()
    publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ad = models.OneToOneField(to="AuthorDetail", to_field="id", on_delete=models.CASCADE, )


class AuthorDetail(models.Model):
    gf = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)


class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class Upload(models.Model):
    file_name = models.CharField(max_length=32)