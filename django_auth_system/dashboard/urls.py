from django.urls import path, include

from .views import index, change_password

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('index/', index),
    path('change_password/', change_password.as_view(), name='change_password'),
]