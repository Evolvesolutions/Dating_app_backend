from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, mail_id, password=None, **extra_fields):
        if not mail_id:
            raise ValueError("The Email must be set")
        mail_id = self.normalize_email(mail_id)
        user = self.model(mail_id=mail_id, **extra_fields)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, mail_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(mail_id, password, **extra_fields)

class UserDetail(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    mail_id = models.EmailField(unique=True)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mail_id'
    REQUIRED_FIELDS = ['name', 'address']

    def __str__(self):
        return self.mail_id
  