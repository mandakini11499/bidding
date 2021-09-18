"""bidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

from badmin import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/',TemplateView.as_view(template_name="badmin_templates/admin_login.html"),name="admin_login"),
    path('admin_check/',views.adminCheck,name="admin_check"),
    path('admin_home/',TemplateView.as_view(template_name="badmin_templates/admin_home.html"),name="admin_home"),
    path('pending_reg/',views.pendingReg,name="pending_reg"),
    path('approved_reg/',views.approveReg,name="approved_reg"),
    path('decline_reg/',views.declineReg,name="decline_reg"),
    path('approve/',views.approve,name="approve"),
    path('decline/',views.decline,name="decline"),
    path('logout_admin/',views.logoutAdmin,name="logout_admin"),
]
