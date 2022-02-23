from django.contrib import admin
from django.urls import include, path
from authapi.api.views import GoogleLogin

urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='google-login')
]
