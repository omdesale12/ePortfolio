from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserRegisterForm,UpdateUserProfile,AddSocial
from django.contrib.auth import get_user_model,authenticate,login,logout
import random
from . models import User,UserProfile,UserSocials
from main.models import portfolio
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


def logoutUser(request):
    if request.method=="POST":
        logout(request)
        return redirect('/')
    else:
        return HttpResponse("$)$) NOT LOGOUT")

def profile(request,user_id):
    user=get_object_or_404(User,user_id=user_id)
    profile=UserProfile.objects.get(user=user)
    socials=UserSocials.objects.filter(user=profile)
    user_portfolio=None
    addsocial=AddSocial()

    if request.method=="POST":
        addsocial=AddSocial(request.POST)
        if addsocial.is_valid():
            user_profile = request.user.userprofile
            social = addsocial.cleaned_data['social']
            existing_entry = UserSocials.objects.filter(user=user_profile, social=social).first()
            if existing_entry:
                # Handle the case when the combination already exists
                addsocial.add_error('social', 'This social media type already exists for this user.')
            else:
                user_social=addsocial.save(commit=False)
                user_social.user=request.user.userprofile
                user_social.save()
                return redirect("/")
            
    try:
        user_portfolio=portfolio.objects.get(user=profile)
    except portfolio.DoesNotExist:
        user_portfolio=None

    context={
        "profile":profile,
        "user":user,
        "socials":socials,
        "addsocial":addsocial,
        "user_portfolio":user_portfolio
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


