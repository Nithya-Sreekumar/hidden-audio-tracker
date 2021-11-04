"""hat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from hatapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.guest_home,name="Ghome"),
    path('reg/',views.guest_reg,name="Greg"),
    path('login/',views.guest_login,name="Glog"),
    path('uhome/',views.user_home,name="Uhome"),
    path('uprofile/',views.user_profile,name="Uprof"),    
    path('compose88/',views.user_compose,name="Ucompose"),
    path('compose/',views.edit,name='exeternal'),
    path('inbox/',views.user_inbox,name='inboxda'),
    path('inbox1/',views.inbox1,name='inbox1da'),
    path('draft/',views.draft,name='inbox1da'),
    path('profileedit/',views.profileedit,name='profileedit'),
]
