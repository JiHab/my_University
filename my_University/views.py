from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from my_University.models import Group, Student
from django.core.context_processors import csrf



def home(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    username = auth.get_user(request).username
    context = {
        'groups': groups,
        'students': students,
        'username': username
    }
    print()
    return render(request, 'home.html', context)


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