from django.urls import path
from django.views.generic import TemplateView

# from .views import (
    # RegisterView,
    # LoginView,
    # LogoutView,
    # VerifyView,
    # ResendView,
    # EmailVerificationView
# )

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [ 
    # path('register/', RegisterView.as_view() , name='register'),

]
