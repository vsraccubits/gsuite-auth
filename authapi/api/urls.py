from django.urls import path
from authapi.api.views import GoogleLogin
from dj_rest_auth.registration.views import SocialAccountListView
from dj_rest_auth.views import LogoutView

urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='google-login'),
    path('list/', SocialAccountListView.as_view(), name='social_account_list'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
]
