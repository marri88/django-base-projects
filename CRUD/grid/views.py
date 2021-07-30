from django.shortcuts import render, redirect
from .forms import EmployerForm
from .models import Employer


def addnew(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass

    else:
        form = EmployerForm()
        return render(request, 'index.html', {'form': form})


def index(request):
    employers = Employer.objects.all()
    return render(request, 'show.html', {'employers': employers})


def edit(request, id):
    employers = Employer.objects.get(id=id)
    return render(request, 'edit.html', {'employers': employers})


def update(request, id):
    employer = Employer.objects.get(id=id)
    form = EmployerForm(request.POST, instance=employer)
    if form.is_valid():
        form.save()
        redirect("/")
        return render(request, 'edit.html', {'employer': employer})

def destroy(request, id):
    employer = Employer.objects.get(id=id)
    employer.delete()
    return redirect("/")
