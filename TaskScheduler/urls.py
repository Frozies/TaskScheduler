"""TaskScheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users.views import UserDeleteView, UserDeactivateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/', include('allauth.urls')),
    url(r'^account/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    url(r'^account/delete/', UserDeleteView.as_view(), name='account_delete'),
    url(r'^account/deactivate/', UserDeactivateView.as_view(), name='account_deactivate'),
]
