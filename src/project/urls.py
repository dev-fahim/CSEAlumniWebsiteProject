"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from admin_site import views as core_views

on_site = False

admin.site.site_header = "Begum Rokeya University / CSE Alumni Association Website"
admin.site.site_title = "Begum Rokeya University / CSE Alumni Association Website"
admin.site.index_title = "Begum Rokeya University / CSE Alumni Association Website"

urlpatterns = [
    path('', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('accounts.api.urls', namespace='accounts')),
    re_path(r'^signup/$', core_views.signup, name='signup'),
    re_path(r'^auth/', include('djoser.urls')),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
            #  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

""""
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
if on_site:
    urlpatterns.append(re_path(r'^', TemplateView.as_view(template_name='index.html')))
"""
