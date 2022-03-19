"""毕业项目 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.static import serve
from django.conf import settings

from django.urls import path,re_path
from app01.views import admin,depart

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # 写管理员的任务
    path('manage/index/',admin.index),
    path('manage/login/',admin.login),
    path('manage/logout/',admin.logout),

    path('depart/list/',depart.list),
    path('depart/add/',depart.add),
    path("depart/<int:nid>/edit/", depart.edit),
    path("depart/<int:nid>/delete/", depart.delete),
]
