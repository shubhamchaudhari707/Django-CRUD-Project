from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistation
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistation(request.POST)
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pw = request.POST.get('passward')
        reg = User(name=nm,email=em,passward=pw)
        reg.save()
        fm = StudentRegistation()
        # if fm.is_valid():
        #     fm.save()
    else:
        fm = StudentRegistation()

    stud = User.objects.all()
    return render(request,'testapp/addshow.html', {'form':fm, 'stu':stud})

# this fuction is delete
def delete_data(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# update data

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        ss = StudentRegistation(request.POST,instance=pi)
        if ss.is_valid:
            ss.save()
    else:
        pi = User.objects.get(pk=id)
        ss = StudentRegistation(instance=pi)

    return render(request,'testapp/updatestudent.html', {'form':ss})







