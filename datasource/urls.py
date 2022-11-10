from django.urls import path
from . import views

urlpatterns = [
    path('immigration/<str:data_id>', views.get_immigration),
    path('category/<str:data_id>', views.get_category),
    path('country/<str:data_id>', views.get_country),
    path('destination/<str:data_id>', views.get_destination),
    path('upload_data_file/<str:db_type>', views.upload_data_file),
]