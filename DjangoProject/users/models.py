from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#from django.contrib.auth import get_user_model
#User = get_user_model()
#get_user_model().objects.get()
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin = False, is_staff = False):
        if not email:
            raise ValueError("Users must have an Email")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        print(email)
        user = self.create_user(
            email,
            password = password,
            is_admin = True,
            
        )
        return user

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True)
    admin       = models.BooleanField(default=False)
    staff      = models.BooleanField(default=False)
    #birthday    = models.DateField(widget=models.DateInput(attrs={'type':'date'}))

    objects = UserManager()

    USERNAME_FIELD = 'email' #username for this User
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    #@login_required
    #def profile(request):
    #    return render(request, 'profile.html')

    #DOUBT HERE
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, todolist):
        return True



class Profile(models.Model):  #class Profile(User):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
def __str__(self):
    return f'{self.user.username} Profile'



