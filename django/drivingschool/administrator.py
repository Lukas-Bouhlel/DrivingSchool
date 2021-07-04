from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def home(request):
    secretary = User.objects.filter(groups__name='Secretary')
    return render(request, 'administrator/index.html', {'secretarylist': secretary})

def secretary(request, id):
    secretary = User.objects.filter(groups__name='Secretary').get(id=id)
    if secretary:
        return render(request, 'administrator/secretary.html', {'secretary': secretary})

def addSecretary(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST['role'])
            user.groups.add(group)
            return redirect('administrator')

    form = UserCreationForm()
    return render(request, 'administrator/form.html', {'form': form})