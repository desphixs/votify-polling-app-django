"""
URL configuration for votify_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# We import 'include' so we can delegate URL routing to our separate app urls.py files.
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Think of this like directing all general foot traffic at the entrance gate
    # directly into our recreational gaming lounge ('polls' app urls).
    path('', include('polls.urls')),
]
