from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    # REQUIRED FUNCTIONS
    def create_user(self, email, username, first_name, last_name, date_of_birth, password=None): # ensure that all required fields are paramaters
        if not email:
            raise ValueError('Users must have an email. ')
        if not username:
            raise ValueError('Users must have a username. ')
        if not first_name:
            raise ValueError('Users must have a first name. ')
        if not last_name:
            raise ValueError('Users must have a last name. ')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth. ')
        
        user = self.model(
            email           = self.normalize_email(email),
            username        = username,
            first_name      = first_name,
            last_name       = last_name,
            date_of_birth   = date_of_birth
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, date_of_birth):
        
        user = self.create_user(
            email           = self.normalize_email(email),
            username        = username,
            password        = password,
            first_name      = first_name,
            last_name       = last_name,
            date_of_birth   = date_of_birth
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    
    user_id = models.AutoField(primary_key=True)

    # required fields
    username            = models.CharField(unique=True, max_length=60)
    date_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    # my required fields
    email               = models.EmailField(unique=True, max_length=60)
    first_name          = models.CharField(max_length=60)
    last_name           = models.CharField(max_length=60)
    date_of_birth       = models.DateField()



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'date_of_birth']

    objects = UserManager() # referencing the User manager created

    def __str__(self):
        return self.email
    
    # REQUIRED FUNCTIONS
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True