
from django.contrib import admin
from django.urls import path
from purniaresultapp.views import home,insert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="homepage"),
    path('insert/',insert,name="insert"),
]
