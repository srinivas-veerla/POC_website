from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import UserTable
from django.db import IntegrityError
# Create your views here.

def login(request):
    if request.method=='POST':
        users=UserTable.objects.filter(empid=request.POST['username'])
        for i in users:
            if i.password==request.POST['password']:# and  i.empid==request.POST['username'] and i.role==request.POST['role']:
                return render(request,'Userhome.html',{'name':i.emp_name})#HttpResponseRedirect('user',{'name':i.emp_name})
        else:
            context={'message':"Check Employee ID, Password or Role!"}
            return render(request,'login.html',context)

    return render(request,'login.html')

def forgotPassword(request):
    if request.method=="POST":
        user=UserTable.objects.filter(email_id__exact=request.POST['email_id'])
        for i in user:
            if i.secret_code==request.POST['s_code']:
                if request.POST['c_password']==request.POST['n_password']:
                    i.password=request.POST['c_password']
                    i.save()
                    context={'message':"Password change successful!"}
                    return render(request,"Login.html",context)
                else:
                    context={'message':"Passwords doesn't match!"}
                    return render(request,'Forgotpass.html',context)
    context={}
    return render(request,'Forgotpass.html',context)

def signup(request):
    if request.method=="POST":
        try:
            if request.POST['password']==request.POST['c_password']:
                user=UserTable(emp_name=request.POST['name'],empid=request.POST['empid'],
                email_id=request.POST['email_id'],password=request.POST['password'],
                proj_manager="Ananda",secret_code=request.POST['empid'][-2:] + 'oct')
                user.save()
                context={'message':"New User created!"}
                return render(request,"Login.html",context) 
        except IntegrityError:
            context={'message':"User exists!"}
            return render(request,"Login.html",context) 
        else:
            context={'message':"Passwords doesn't match"}
            return render(request,"Signup.html",context)     
    context={}
    return render(request,'Signup.html',context)

def logged(request):
    return render(request,'Userhome.html',)