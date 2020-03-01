"""ajaxproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from demoapp import views
from demoapp.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # rest framework urls.py file include
    path('admin/', admin.site.urls),
    path('insert/', views.StudentView, name='insert'),
    path('stud-api', views.StudView.as_view(), name='stud-api'),
    path('stud-api<int:pk>', views.StudViewCrud.as_view(), name='stud-api'),

    # path('', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('', account_view, name="home"),

    path('register/', registration_view, name='register'),

]
