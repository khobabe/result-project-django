
from django.contrib import admin
from django.urls import path
from rms.views import home,insertFunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="homepage"),
    path('insert/',insertFunction,name="insert")
]
