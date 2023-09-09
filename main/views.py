from django.shortcuts import render,get_object_or_404,HttpResponse
from user.models import UserProfile,UserSocials,User
from .models import portfolio
# Create your views here.
def homePage(request):
    portfolios=portfolio.objects.all()
    context={
        "portfolios":portfolios,
    }
    return render(request, "main/homePage.html",context)

def eportfolio(request,email):
    # user=UserProfile.objects.get(user=request.user.email)
    user=get_object_or_404(User,email=email)
    user_profile=UserProfile.objects.get(user=user)
    user_portfolio=None

    try:
        user_portfolio=portfolio.objects.get(user=user_profile)
        insta=UserSocials.objects.filter(user=user_profile, social=1)
    
        context={
            "user":user,
            "user_profile":user_profile,
            "insta":insta,
            "user_portfolio":user_portfolio
        }
        return render(request, "main/index.html",context)
    except portfolio.DoesNotExist:
        return HttpResponse("PORTFOLIO NOT FOUND")

        







    