"""app_emap URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 

from emap.views import home, aboutus, get_chargers, get_connector_types
from accounts.views import login_view, logout_view, sign_up,password_reset_request


urlpatterns = [
    path('admin/', admin.site.urls),

    #emap
    path('', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('get-chargers/', get_chargers, name='get_chargers'),
    path('get-connector-types/', get_connector_types, name='get_connector_types'),

    #accounts
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', sign_up, name='signup'),

    # password management
    # path('accounts/', include('django.contrib.auth.urls')),

    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/passwords/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/passwords/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/passwords/password_reset_complete.html'), name='password_reset_complete'),  
]
