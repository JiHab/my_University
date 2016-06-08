from django.contrib.auth.models import User
from django.db import models

defuser = User.objects.get(id=1)

class Group(models.Model):
    name = models.CharField(max_length=100)
    monitor = models.ForeignKey('Student', blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=300)
    date_birth = models.DateField('Date of birth')
    group_s = models.ForeignKey(Group, blank=True,null=True)
    user = models.ForeignKey(User, blank=True, null=False)
    email = models.EmailField(max_length=254)

    # def check_student
    def __str__(self):
        return self.name

