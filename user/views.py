from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserRegisterForm,UpdateUserProfile
from django.contrib.auth import get_user_model,authenticate,login,logout
import random
from . models import User,UserProfile
User=get_user_model()
# Create your views here.

def home(request):
    return render(request, "user/home.html")

def register(request):
    form=UserRegisterForm()
       
    u_id=random.randint(0,10000)
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.instance.user_id = u_id
            form.save()
            return redirect("/")
        
    context={
        "form":form,
    }   

    return render(request, "user/register.html",context)

def loginUser(request):
    
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(request, username=email,password=password)

        if User is not None:
            login(request,user)
            print(request.user)
            return redirect('/')

    return render(request, "user/loginUser.html")


def logoutUser(request):
    if request.method=="POST":
        logout(request)
        return redirect('/')
    else:
        return HttpResponse("$)$) NOT LOGOUT")

def profile(request,user_id):
    user=get_object_or_404(User,user_id=user_id)
    profile=UserProfile.objects.get(user=user)
    print(profile)
    context={
        "profile":profile,
        "user":user,
    }
    return render(request,"user/profile.html",context)

def updateProfile(request,user_id):
    if request.user==get_object_or_404(User,user_id=user_id):
        user=get_object_or_404(User,user_id=user_id)
        profile=UserProfile.objects.get(user=user)

        form=UpdateUserProfile()
        context={
            'form':form
        }

        if request.method=="POST":
            form=UpdateUserProfile(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('/')
    else:
        return HttpResponse("<H1>404 NOT ALLOWED</H1>")
    return render(request,"user/updateProfile.html",context)