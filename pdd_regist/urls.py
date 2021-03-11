"""pdd_regist URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from register import views



urlpatterns = [
    url(r'^$', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('update_eng/', views.update_eng, name='update_eng'),
    # url(r'^save_emp', views.save_emp),
    # url(r'^datatable/$', views.UsersListJson, name='order_list_json'),
    path('regist/<int:PK_Course_D>/', views.course_title, name='course_title'),
    path('detial/<int:PK_Course_D>/', views.course_detial, name='course_detial'),
    path('detail_km/<int:PK_Course_D>/', views.course_KM, name='course_KM'),
    path('detail_km2/<int:PK_Course_D>/', views.course_KM2, name='course_KM2'),
    path('detail_km3/<int:PK_Course_D>/', views.course_KM3, name='course_KM3'),
    path('detail_km4/<int:PK_Course_D>/', views.course_KM4, name='course_KM4'),
    path('course_SD_HQ/<int:PK_Course_D>/', views.course_SD_HQ, name='course_SD_HQ'),
    path('course_register_SD_HQ/<int:PK_Course_D>/', views.course_register_SD_HQ, name='course_register_SD_HQ'),
    path('course_SD_RE/<int:PK_Course_D>/', views.course_SD_RE, name='course_SD_RE'),
    url(r'course_base', views.course_base, name='course_base'),
    path('admin/', admin.site.urls),

]