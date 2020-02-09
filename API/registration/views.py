from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import FORMNAME
from . import forms


# Create your views here.
def register(request):
    formm=forms.formname()
    return render(request,'register.html',{'form':formm})

def submit(request):
    Name=request.POST.get('name',False)
    Email=request.POST.get('email',False)
    Password=request.POST.get('password',False)
    details=FORMNAME(NAME=Name,EMAIL=Email,PASSWORD=Password)
    details.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)

def index(request):
    return render(request,'index.html')

def login(request):
        logform = forms.login()
        return render(request,'login.html',{'log':logform})



def login_user(request):
    Email=request.POST.get('Email',False)
    Pass = request.POST.get('Password',False)
    obj=FORMNAME.objects.all().filter(EMAIL=Email).values("NAME")
    return render(request,'welcome.html',{'well': obj})
    '''next=request.GET.get('next')
    logform = login(request.POST or None)
    if obj.is_valid():
        usern = obj.cleaned_data.get('usermail')
        passwod = obj.cleaned_data.get('passwd')
        user=authenticate(username=usern,password=passwod)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request,'welcome.html',{'well':obj})'''

