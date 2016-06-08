from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from my_University.models import Group, Student
from django.core.context_processors import csrf

from my_University.my_un import check_registration_data


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

def registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        # new_user_form = UserCreationForm(request.POST)
        # username = request.POST.get('username', '')
        # password1 = request.POST.get('password1', '')
        # password2 = request.POST.get('password2', '')
        # b_date = request.POST.get('b_date', '')
        # email = request.POST.get('email', '')
        # name = request.POST.get('name', '')
        # print(username, password1, password2, email, b_date, name)
        # if new_user_form.is_valid():
        #     new_user_form.save()
        #     new_user = auth.authenticate(new_user_form.changed_data['username'], password=new_user_form.cleaned_data['password'])
        #     auth.login(request, new_user)
        #     return redirect('/')
        # else:
        #     args['form'] = new_user_form
        c = check_registration_data(request)
        print(c)
        return render_to_response('reg.html', args)
    return render_to_response('reg.html', args)