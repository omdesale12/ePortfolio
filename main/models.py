from django.db import models
from user.models import UserProfile

# Create your models here.
class portfolio(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_created=True)
    description=models.TextField()

    def __str__(self):
        return str(self.user)
    
class resume(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    resume_file=models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume_file.name
    
class Skills(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)

class Education(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    university=models.CharField(max_length=255)
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_year_start = models.PositiveIntegerField()
    graduation_year_end = models.PositiveIntegerField()
    grade=models.FloatField()

class Certifications(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    certification_url = models.FileField(upload_to="certificates/")

class WorkExperience(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    employment_period = models.CharField(max_length=100)  # You can use a CharField for simplicity
    job_description = models.TextField()
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
class Projects(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    project_url = models.URLField(blank=True, null=True)
    github_repository = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title