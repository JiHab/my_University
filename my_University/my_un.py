from my_University.models import Group, Student


def get_groups():
    groups = Group.objects.all()
    for gr in groups:
        students = Student.objects.filter(group_s = gr)
        print(students)
