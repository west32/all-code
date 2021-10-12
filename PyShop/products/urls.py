from django.urls import path
from .import views


urlpatterns = [
    path("", views.old),
    path("products/new", views.new)
]