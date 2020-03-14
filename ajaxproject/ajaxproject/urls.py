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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from demoapp import views
from demoapp.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,

    registration_view1,
    logout_view1,
    login_view1,
    account_view1,
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
    path('accounts/login/', login_view, name="login"),
    path('', account_view, name="home"),

    path('home', account_view1, name="home1"),
    path('register1/', registration_view1, name="register1"),
    path('logout1/', logout_view1, name="logout1"),
    path('login1/', login_view1, name="login1"),
    path('accounts/login/', login_view1, name="login1"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
