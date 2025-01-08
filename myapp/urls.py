from django.urls import path
from .views import upload_csv_view

urlpatterns = [
    path('upload-csv/', upload_csv_view, name='upload-csv'),
]