from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        user_id,
        email,
        full_name,
        password=None,
        is_active=True,
        is_staff=False,
        is_admin=False,
    ):
        if not user_id:
            raise ValueError("Id required")
        if not password:
            raise ValueError("Password Req")
        if not full_name:
            raise ValueError("Fullname Req")

        user_obj = self.model(
            user_id=user_id,
            full_name=full_name,
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, user_id, email, full_name, password=None):
        user = self.create_user(
            user_id, email, full_name, password=password, is_staff=True
        )
        return user

    def create_superuser(self, user_id, email, full_name, password=None):
        user = self.create_user(
            user_id,
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.PositiveIntegerField(unique=True)
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_id","full_name"]

    objects = CustomUserManager()

    def __str__(self):
        return (
            str(self.user_id) + str("-->") + str(self.full_name) + str("-->") + str(self.email)
        )

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=13)
    profile_image=models.ImageField(default='default1.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.email

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_UserProfile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_UserProfile,sender=User)