from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def home(request):
    for group in request.user.groups.all():
        if group.name == "Secretary":
            return redirect('secretary')
        if group.name == "Student":
            return redirect('studentplanning')
        if group.name == "Administrator":
            return redirect('administrator')
        if group.name == "Admin":
            return redirect('/admin')
        if group.name == "Instructor":
            return redirect('instructor')