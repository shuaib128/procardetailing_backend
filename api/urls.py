from django.urls import path
from .views import (Mainview)

urlpatterns = [
    path('', Mainview.as_view())
]