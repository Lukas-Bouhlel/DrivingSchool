from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from drivingapp.models import Planning
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    instructors = User.objects.filter(groups__name='Instructor')
    students = User.objects.filter(groups__name='Student')
    return render(request, 'secretary/index.html', {'instructorslist': instructors, 'studentslist': students})

@login_required
def student(request, id):
    student = User.objects.filter(groups__name='Student').get(id=id)
    studentPlannings = Planning.objects.filter(id_student=id)
    instructor = User.objects.filter(groups__name='Instructor')
    if student:
        return render(request, 'secretary/student.html', {'student': student, 'plannings': studentPlannings, 'instructors': instructor})

@login_required
def instructor(request, id):
    instructor = User.objects.filter(groups__name='Instructor').get(id=id)
    instructorPlannings = Planning.objects.filter(id_instructor=id)
    student = User.objects.filter(groups__name='Student')
    if student:
        return render(request, 'secretary/instructor.html', {'instructor': instructor, 'plannings': instructorPlannings, 'studentslist': student})

@login_required
def addUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST['role'])
            user.groups.add(group)
            return redirect('secretary')

    form = UserCreationForm()
    return render(request, 'secretary/form.html', {'form': form})

@login_required
def deleteUser(request):
    User.objects.filter(username=request.POST['username']).delete()
    return redirect('secretary')

@login_required
def deletePlanning(request, id):
    planning = Planning.objects.get(id=id)
    if planning:
        planning.delete()
        return redirect('secretary')

@login_required
def delete(request, id):
    user = User.objects.get(id=id)
    if user:
        user.delete()
        return redirect('secretary')