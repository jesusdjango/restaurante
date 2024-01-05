from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdate.as_view(), name="profile"),
    path("profile/email/", EmailUpdate.as_view(), name="profile_email"),
]

#path("accounts/", include("django.contrib.auth.urls")), 
    #Con esto en el urls.py(principal) te mete 8 urls que ya no tienes que definir
    #login, logout, password_change, password_change_done, 
    #password_reset, password_reset_done, password_reset-confirm, password_reset_complete
    
  

