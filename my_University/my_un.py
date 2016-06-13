import re

from my_University.models import Group, Student, User


def get_groups():
    groups = Group.objects.all()
    for gr in groups:
        students = Student.objects.filter(group_s = gr)
        print(students)


def get_user_by_email(email):
    # print(email)
    try:
        user = User.objects.get(email=email.lower())
        return user
    except:
        return None

def check_data_and_register(request):

    r = {}
    r['error'] = False
    r['error_text'] = ''
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    b_date = request.POST.get('b_date', '')
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')
    groupstr = request.POST.get('group', '')
    group = Group.objects.filter(name=groupstr)[0]
    em = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.lstrip().rstrip())

    if em is None and email != '':
        r['error'] = True
        r['error_text'] = 'Email si invalid'
        return r

    if username.lstrip().rstrip() is '':
        r['error'] = True
        r['error_text'] = 'Enter your nickname'
        return r
    user_ = User.objects.filter(username=username)
    if len(user_) > 0:
        r['error'] = True
        r['error_text'] = 'User with nickname ' + username + ' allready exist!'
        return r
    if password1 != password2:
        r['error'] = True
        r['error_text'] = 'Pass1 <> Pass2'
        return r
    user_ = User.objects.filter(email=email)
    if len(user_) > 0:
        r['error'] = True
        r['error_text'] = 'User with email ' + email + ' allready exist!'
        return r
    if name.lstrip().rstrip() is '' or username.lstrip().rstrip() is '':
        r['error'] = True
        r['error_text'] = 'Enter your name or nickname'
        return r

    user = User()
    user.username = username
    user.email = email.lower()
    # user.password = password1
    user.set_password(password1)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    try:
        user.save()
    except:
        r['error'] = True
        r['error_text'] = 'Somethitg wrong with user(9'
        return r

    student = Student()
    student.name = name
    student.date_birth = b_date
    student.user = user
    student.group_s = group
    try:
        student.save()
    except:
        r['error'] = True
        r['error_text'] = 'Somethitg wrong with student(9'
        return r

    r['user'] = user
    r['student'] = student

    return r
