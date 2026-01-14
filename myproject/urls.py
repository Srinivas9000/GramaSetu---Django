"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp.views import home
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("panchaiyeti/",panchaiyeti,name="panchaiyeti"),
    path("temples/",temples,name="temples"),
    path("tourism/",tourism,name="tourism"),
    path("farming/",farming,name="farming"),
    path("school/",school,name="school"),
    path("sports/",sports,name="sports"),
    path("services/",services,name="services"),
    path('logout/', logout_view, name='logout'), 
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
