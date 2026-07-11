from urllib import request 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from django.shortcuts import redirect, render
from .forms import StudentRegistration
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email']
           pw = fm.cleaned_data['password']
           reg = User(name=nm, email=em, password=pw)
           reg.save()
           return redirect('addandshow')
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

def update_data(request, id):
    pi = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')
    else:
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')