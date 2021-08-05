#config/urls.py
from django.contrib import admin
from django.urls import path, include
from . import index

urlpatterns = [

    #path('admin/', admin.site.urls),
    #path('', include('.urls')),
    path('', index.signin),
    path('signup.html', index.signup),
    path('signin.html', index.signin),
]
