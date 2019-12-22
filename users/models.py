from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    # REQUIRED FUNCTIONS
    def create_user(self, email, username, password=None): # ensure that all required fields are paramaters
        if not username:
            raise ValueError('Users must have an email. ')
        if not username:
            raise ValueError('Users must have a username. ')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    

    # REQUIRED FIELDS
    username            = models.CharField(unique=True, max_length=60)
    date_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    email               = models.EmailField(unique=True, max_length=60)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager() # referencing the User manager created

    def __str__(self):
        return self.email
    
    # REQUIRED FUNCTIONS
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True