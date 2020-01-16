from django.urls import path
from accounts.api.views import ProfileCardDetailsAPIView

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileCardDetailsAPIView.as_view()),
]
