from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, Group, Permission

class MyUser(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    ADMIN = 1
    USER = 2

    ROLES = (
        (ADMIN, 'Admin User'),
        (USER, 'User'),
    )

    # Add other fields as needed for your user model. For example, phone number, address etc.
    # username, email, password
    role = models.IntegerField(
        choices=ROLES, default=ROLES[1][0], blank=True, null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, default=GENDER_CHOICES[0], max_length=20, blank=True, null=True)

    # Override the groups and user_permissions fields with unique related_name
    groups = models.ManyToManyField(Group,
        related_name='myuser_set',
        blank=True,
        help_text='Groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username


class DemoFiles(models.Model):
    pdf = models.FileField(upload_to='DemoFiles', null=True, blank=True)
    image = models.FileField(upload_to='DemoFiles', null=True, blank=True)


class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='Profile', blank=True, null=True)

    def __str__(self):
        return self.name