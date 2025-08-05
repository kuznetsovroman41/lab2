from django.urls import path
from .views.register import RegisterView
from .views.login import CustomLoginView
from .views.logout import CustomLogoutView
from .views.subscribe import SubscribeToggleView
from .views import UserSearchView, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('search/', UserSearchView.as_view(), name='user_search'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    path('subscribe/<str:username>/', SubscribeToggleView.as_view(), name='subscribe_toggle'),
]
