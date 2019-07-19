from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,login,password):
        user = self.model(
            login=login.lower(),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,login, password):
        user = self.create_user(login,password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    class Meta:
        db_table = 'auth_user'
        abstract = False

    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    sur_name = models.CharField(max_length=255, blank=True)
    fath_name = models.CharField(max_length=255, blank=True)
    age = models.CharField(max_length=255, blank=True)
    date_of_reg = models.DateField(auto_created=True, auto_now=True)
    link = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(blank=True, upload_to='main/users')
    subscribes = models.ManyToManyField("self", blank=True)
    city = models.CharField(max_length=255, blank=True)  # need change on models.ForeignKey

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'login'

    objects = MyUserManager()

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_created=True)


class Article(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='main/articles', blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_created=True, auto_now=True)
    comments = models.ManyToManyField(Comment)


