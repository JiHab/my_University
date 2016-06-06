from django.shortcuts import render
from django.contrib import auth
from my_University.models import Group, Student


def home(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    print(auth.get_user(request))
    context = {
        'groups': groups,
        'students': students,
        'username': auth.get_user(request)
    }
    print()
    return render(request, 'home.html', context)