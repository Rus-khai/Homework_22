from django.urls import path

# from . import views
from .views import CatalogListView, CatalogDetailView, HomeView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CanUnpublishProductView

app_name = "catalog"


class DeleteProductView:
    pass


urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("catalog_list/", CatalogListView.as_view(), name="catalog_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", CatalogDetailView.as_view(), name="detail_product"),
    path("product_form/", ProductCreateView.as_view(), name="product_form"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/can_unpublish/", CanUnpublishProductView.as_view(), name="can_unpublish_product"),
]
