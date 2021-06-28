from django.db import models
from django.contrib.auth.models import User


class Tree(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    depth = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    GENDER_CHOICES = (
        ('U', 'Undefined'),
        ('M', 'Male'),
        ('F', 'Female')
    )
    firstname = models.CharField(max_length=255, default="unknown")
    secondname = models.CharField(max_length=255, null=True, blank=True)
    thirdname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, default="unknown")
    birthdate = models.DateTimeField(null=True, blank=True)
    deathdate = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    desc = models.TextField(null=True, blank=True)
    url = models.URLField(null = True, blank = True)

    def __str__(self):
        return f"{self.lastname} {self.firstname} b.{self.birthdate}"


class Relationship(models.Model):
    """Direct relation between two persons"""
    RELATIONSHIP_CHOICES = (
        ('P', 'Parent-child'),
        ('C', 'Couple')
    )
    type = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES)
    desc = models.TextField(null=True, blank=True)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    a = models.ForeignKey(Person, related_name='a', on_delete=models.PROTECT)
    b = models.ForeignKey(Person, related_name='b', on_delete=models.PROTECT)

    def __str__(self):
        if self.type == 'P':
            return f"Parent = {self.a.__str__()}/ Child = {self.b.__str__()}"
        else:
            return f"Partner = {self.a.__str__()}/ Partner = {self.b.__str__()}"


class Event(models.Model):
    """An event affects one ore more persons at the same time"""
    EVENT_CHOICES = (
        ('BI', 'Birth'),
        ('DE', 'Death'),
        ('MA', 'Marriage'),
        ('SE', 'Separation'),
        ('DI', 'Divorce'),
        ('AD', 'Adoption'),
        ('MO', 'Change of address'),
        ('BM', 'Bar or bat mitsvah'),
        ('CO', 'Communion'),
        ('OT', 'Other')
    )
    type = models.CharField(max_length=2, choices=EVENT_CHOICES)
    desc = models.TextField(null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(null = True, blank = True)
    protagonist = models.ManyToManyField(Person, related_name='events')


