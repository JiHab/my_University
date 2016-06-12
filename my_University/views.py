from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from my_University.models import Group, Student
from django.core.context_processors import csrf

from my_University.my_un import check_data_and_register


def home(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    user = auth.get_user(request)
    username = user.username
    is_admin = user.is_superuser
    context = {
        'groups': groups,
        'students': students,
        'username': username,
        'is_admin': is_admin
    }
    for gr in groups:
        print(gr.pk)

    return render(request, 'dial.html', context)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                return redirect('/')
        else:
                    args['login_error'] = "user is not found"
                    return render_to_response('login.html', args)
    else:
            return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    args = {}
    args.update(csrf(request))
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    args.update(context)
    # args['form'] = UserCreationForm()
    if request.POST:
        result = check_data_and_register(request)
        if result['error'] is False:
            user = authenticate(username=result['user'].username, password=result['user'].password)
            auth.login(request, result['user'])
            return redirect('/')
        args.update(result)
        return render_to_response('reg.html', args)
    return render_to_response('reg.html', args)


def details(request, id):
    print(id)
    group = Group.objects.get(id=id)
    print(group)
    students = Student.objects.filter(group_s=group)
    # print(students)
    user = auth.get_user(request)
    username = user.username
    # students = Student.objects.all()
    # user = auth.get_user(request)
    # username = user.username
    is_admin = user.is_superuser
    context = {
        'monitor': group.monitor,
        'students': students,
        'username': username,
        'is_admin': is_admin
    }

    return render(request, 'details.html', context)





































