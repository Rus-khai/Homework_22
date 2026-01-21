from django.urls import path

# from . import views
from .views import CatalogListView, CatalogDetailView, HomeView, ContactsView

app_name = "catalog"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("catalog_list/", CatalogListView.as_view(), name="catalog_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", CatalogDetailView.as_view(), name="detail_product"),
]
