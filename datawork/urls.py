from django.urls import path
from datawork.views import Home

urlpatterns = [
    path("", Home.as_view(), name="homepage"),
]
