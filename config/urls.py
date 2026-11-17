from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.exec_home, name='exec_home'),
    path('Executive/exec_header/', views.exec_header, name='exec_header'),
    path("Executive/constitution/", views.constitution, name="constitution"),
    path("Executive/chairpersons/", views.chairpersons, name="chairpersons"),
]