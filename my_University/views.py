from django.shortcuts import render

from my_University.models import Group, Student


def home(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    print(students)
    context = {
        'groups': groups,
        'students': students
    }

    return render(request, 'home.html', context)