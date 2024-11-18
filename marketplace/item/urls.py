from django.urls import path,include

from . import views

app_name = "item"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("additem/", views.newitem, name="additem"),
    path("dashboard/",include('dashboard.urls')),

]
