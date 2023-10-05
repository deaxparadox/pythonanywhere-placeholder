from django.urls import path 

from . import views

urlpatterns = [
    path("api/", views.ListView.as_view(), name="list"),
    path("api/<int:id>/", views.get_user_info_view, name="list")
]
