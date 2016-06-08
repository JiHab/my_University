from my_University.models import Group, Student, User


def get_groups():
    groups = Group.objects.all()
    for gr in groups:
        students = Student.objects.filter(group_s = gr)
        print(students)


def check_registration_data(request):
    l = []
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    b_date = request.POST.get('b_date', '')
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')

    user_ = User.objects.filter(username=username)

    if len(user_) > 0:
        return 'User with nickname ' + username + ' allready exist!'
    if password1 != password2:
        return('Pass1 <> Pass2')
    user_ = User.objects.filter(email=email)
    if len(user_) > 0:
        return 'User with email ' + email + ' allready exist!'
    if name.lstrip().rstrip() is '' or username.lstrip().rstrip() is '':
        return 'Enter your name or nickname'
    return True
