from django.urls import path
from django.views.generic import TemplateView

# from homeapp.views import (
    # RegisterView,
    # LoginView,
    # LogoutView,
    # VerifyView,
    # ResendView,
    # EmailVerificationView
# )

from django.contrib.auth.views import (
	LoginView,
	LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [ 
    path('', LoginView.as_view() , name='login'),
    # path('register/', RegisterView.as_view() , name='register'),

]
