from django.shortcuts import render,HttpResponse,redirect
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model,authenticate,login,logout
User=get_user_model()
# Create your views here.
def register(request):
    form=UserRegisterForm()
       
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context={
        "form":form,
    }   

    return render(request, "user/register.html",context)