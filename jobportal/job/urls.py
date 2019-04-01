from django.contrib import admin
from django.urls import path
from .views import UserJobView

urlpatterns = [
    path('jobportal/', UserJobView),
    path('admin/', admin.site.urls),
]