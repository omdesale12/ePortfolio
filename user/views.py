from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model,authenticate,login,logout
import random
from . models import User,UserProfile
User=get_user_model()
# Create your views here.
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


def profile(request,user_id):
    user=get_object_or_404(User,user_id=user_id)
    profile=UserProfile.objects.get(user=user)
    print(profile)
    context={
        "profile":profile,
        "user":user,
    }
    return render(request,"user/profile.html",context)