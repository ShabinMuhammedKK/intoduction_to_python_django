from django.urls import path
from . import views

app_name = "dashboard"


urlpatterns = [
    path("", views.listItems, name="listItems"),
    path("editItems/<int:pk>/", views.editItems, name="editItems"),
    path("delete/<int:pk>/", views.deleteItem, name="deleteItem"),
]
