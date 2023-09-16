from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserRegisterForm,UpdateUserProfile,AddSocial,AddPortfolio,AddEducation,AddResume
from django.contrib.auth import get_user_model,authenticate,login,logout
import random
from . models import User,UserProfile,UserSocials
from main.models import portfolio,resume
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
    user_resume=None
    addsocial=AddSocial()
    addPortfolio=AddPortfolio()
    addEducation=AddEducation()
    

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
    try:
        user_resume=resume.objects.get(user=profile)
    except resume.DoesNotExist:
        user_resume=None

    context={
        "profile":profile,
        "user":user,
        "socials":socials,
        "addsocial":addsocial,
        "user_portfolio":user_portfolio,
        "user_resume":user_resume,
        'addPortfolio':addPortfolio,
        'addEducation':addEducation,
    }
    return render(request,"user/profile.html",context)

def updateProfile(request,user_id):
    if request.user==get_object_or_404(User,user_id=user_id):
        user=get_object_or_404(User,user_id=user_id)
        profile=UserProfile.objects.get(user=user)
        form=UpdateUserProfile(instance=profile)
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

def portfolio_details(request,user_id):
    if request.user==get_object_or_404(User,user_id=user_id):
        user=get_object_or_404(User,user_id=user_id)
        profile=get_object_or_404(UserProfile,user=user)
        user_portfolio=portfolio.objects.get(user=profile)
        addResume=AddResume()

        user_data = UserProfile.objects.select_related(
        'portfolio'
        ).prefetch_related(
            'resume_set',
            'skills_set',
            'education_set',
            'certifications_set',
            'workexperience_set',
            'projects_set'
        ).get(user=request.user)
        
        context={
            "user_portfolio":user_portfolio,
            "profile":profile,
            "user_data":user_data,
            'addResume':addResume,
            
        }
        return render(request, 'user/portfolio_details.html',context)
    else:
        return HttpResponse("NOT ALLOWED")
    

def addPortfolio(request):
    user_profile=UserProfile.objects.get(user=request.user)
    if request.method=="POST":
        addPortfolioForm=AddPortfolio(request.POST)
        addEducationForm=AddEducation(request.POST)

        addPortfolioForm.user=user_profile
        addEducationForm.user=user_profile
        if addPortfolioForm.is_valid() and addEducationForm.is_valid():
            addPortfolioForm.instance.user=user_profile
            addEducationForm.instance.user=user_profile
            addPortfolioForm.save()
            addEducationForm.save()
            return redirect('/')
           
    return HttpResponse("ADD")


def addResume(request):
    user_profile=UserProfile.objects.get(user=request.user)
    if request.method=="POST":
        addResumeForm=AddResume(request.POST,request.FILES)

        addResumeForm.instance.user=user_profile
        if addResumeForm.is_valid():
            addResumeForm.instance.user=user_profile
            print(user_profile)
            addResumeForm.save()
            return redirect('/')
        
    return HttpResponse("ADD RESUME")