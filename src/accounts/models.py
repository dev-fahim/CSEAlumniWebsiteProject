from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
date_format = 'The date format should be yyyy-mm-dd'


class Account(models.Model):
    SESSIONS_CHOICE = (
        ('2007-2008', '2007-2008'),
        ('2008-2009', '2008-2009'),
        ('2009-2010', '2009-2010'),
        ('2010-2011', '2010-2011'),
        ('2011-2012', '2011-2012'),
        ('2012-2013', '2012-2013'),
        ('2013-2014', '2013-2014'),
        ('2014-2015', '2014-2015'),
        ('2015-2016', '2015-2016'),
        ('2016-2017', '2016-2017'),
        ('2017-2018', '2017-2018'),
        ('2018-2019', '2018-2019'),
        ('2019-2020', '2019-2020'),
        ('2020-2021', '2020-2021'),
    )
    DEPARTMENT_CHOICE = (
        ('CSE', 'Computer Science and Engineering'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True, help_text=date_format)

    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICE, null=True)
    intake = models.PositiveSmallIntegerField(null=True)
    graduation_year = models.PositiveSmallIntegerField(null=True)
    session = models.CharField(choices=SESSIONS_CHOICE, max_length=50, null=True)

    profile_picture = models.ImageField(null=True)

    phone_number = PhoneNumberField(max_length=255, null=True)
    present_address = models.TextField(null=True)
    permanent_address = models.TextField(null=True)
    email = models.EmailField(null=True)

    objects = models.QuerySet()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class JobDetail(models.Model):
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='jobs')

    job_from = models.DateField(help_text=date_format)
    job_to = models.DateField(null=True, blank=True, help_text=date_format)
    currently = models.BooleanField(default=False)

    designation = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    institute_type = models.CharField(max_length=255)
    institute_website = models.URLField()
    institute_address = models.TextField()

    objects = models.QuerySet()

    def __str__(self):
        return f'{self.institute_name} / {self.designation}'


class SocialLink(models.Model):
    accounts = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='social')

    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    quora = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    stack_overflow = models.URLField(null=True, blank=True)
    skype = models.URLField(null=True, blank=True)

    objects = models.QuerySet()

    def __str__(self):
        return self.accounts.__str__()
