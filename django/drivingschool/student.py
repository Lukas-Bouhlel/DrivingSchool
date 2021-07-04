from django.shortcuts import render
from drivingapp.models import Planning
from django.contrib.auth.models import User
from drivingapp.forms import PlanningForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def getPlanning(request):
    studentPlannings = Planning.objects.filter(id_student=request.user.id)
    instructor = User.objects.filter(groups__name='Instructor')
    return render(request, "student/planning.html", {"plannings": studentPlannings, 'instructors': instructor})

@login_required
def renderForm(request, id):
    if request.method == "POST":
        form = PlanningForm(request.POST)
        if form.is_valid():
            planning = Planning()
            planning.id_student = form.data['id_student']
            planning.id_instructor = request.user.id
            planning.lieu = form.data['lieu']
            planning.date = form.data['date']
            planning.heure = form.data['heure']
            planning.save()
            return redirect('instructor')
    else:
        form = PlanningForm()
    return render(request, "student/form.html", {"form": form, "studentId": id})