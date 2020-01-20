from django.urls import path
from accounts.api.views import (
    ProfileCardDetailsAPIView,
    AlumniProfileListAPIView,
    ProfileDetailsAPIView,
    AlumniProfileDetailsAPIView,
    SocialLinkDetailsAPIView,
    SocialLinkCreateAPIView,
    JobListAPIView,
    JobCreateAPIView,
    JobDetailsAPIView
)

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileDetailsAPIView.as_view()),
    path('profile/jobs/', JobListAPIView.as_view()),
    path('profile/jobs/create/', JobCreateAPIView.as_view()),
    path('profile/jobs/<int:pk>/', JobDetailsAPIView.as_view()),
    path('profile/socials/', SocialLinkDetailsAPIView.as_view()),
    path('profile/socials/create/', SocialLinkCreateAPIView.as_view()),
    path('profile-card/', ProfileCardDetailsAPIView.as_view()),
    path('profiles-recent-alumni/', AlumniProfileListAPIView.as_view()),
    path('profiles-recent-alumni/<int:pk>/', AlumniProfileDetailsAPIView.as_view()),
]
