from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("catalog_list/", views.catalog_list, name="catalog_list"),
    path("contacts/", views.contacts, name="contacts"),
    path("products/<int:product_id>/", views.view_product, name="view_product"),
    ]
