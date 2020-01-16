from django.contrib import admin
from accounts.models import Account, JobDetail, SocialLink
# Register your models here.

admin.site.register(Account)
admin.site.register(JobDetail)
admin.site.register(SocialLink)
