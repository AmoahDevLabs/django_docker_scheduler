from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.SignUpView.as_view(), name="home"),
    path('sign-in/', views.SignInView.as_view(), name="sign_in"),
    path('sign-out/', views.sign_out, name="sign_out"),
    path('account/', views.AccountView.as_view(), name="account"),
]
