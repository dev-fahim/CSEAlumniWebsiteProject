from django.contrib import admin
from accounts.models import Account, JobDetail, SocialLink

# Register your models here.


class JobDetailInline(admin.StackedInline):

    model = JobDetail
    extra = 1


class SocialLinkInline(admin.StackedInline):

    model = SocialLink


class AccountAdmin(admin.ModelAdmin):

    inlines = (JobDetailInline, SocialLinkInline)

    def get_queryset(self, request):
        if request.user.is_superuser is False:
            return Account.objects.filter(user=request.user)
        return super(AccountAdmin, self).get_queryset(request)

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser is False:
            return 'user',
        return []

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser is False:
            obj.user = request.user
            obj.save()
        return super(AccountAdmin, self).save_model(request, obj, form, change)


admin.site.register(Account, AccountAdmin)
