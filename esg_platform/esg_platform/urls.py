from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('upload/', include('ingestion.urls')),
    path("records/", include("records.urls")),
]

