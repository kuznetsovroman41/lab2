from django.urls import path
from accounts.views.register import RegisterView
from accounts.views.login import CustomLoginView
from accounts.views.logout import CustomLogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
