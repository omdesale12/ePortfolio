from django.contrib import admin
from . models import User,UserProfile,SocialMediaType,UserSocials
# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(SocialMediaType)
admin.site.register(UserSocials)

