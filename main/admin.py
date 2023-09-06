from django.contrib import admin
from .models import portfolio,resume,Skills,Education,WorkExperience,Projects,Certifications
# Register your models here.
admin.site.register(portfolio)
admin.site.register(resume)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Projects)
admin.site.register(Certifications)