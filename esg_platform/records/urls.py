from django.urls import path
from .views import get_records

urlpatterns = [
    path("", get_records, name="get-records"),
]