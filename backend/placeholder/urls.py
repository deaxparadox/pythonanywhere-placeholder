from django.urls import path 

from . import views 
from .api_v1 import urls as api_urls


app_name = "placeholder"

urlpatterns = [
    path("<int:id>/", views.get_user, name="index"),
    path("", views.index, name="index"),
    # 
]  + api_urls.urlpatterns
