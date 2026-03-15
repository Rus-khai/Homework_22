from django.urls import path
from django.views.decorators.cache import cache_page

# from . import views
from .views import CatalogListView, CatalogDetailView, HomeView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CanUnpublishProductView, ProductsByCategoryView

app_name = "catalog"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("catalog_list/", CatalogListView.as_view(), name="catalog_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60)(CatalogDetailView.as_view()), name="detail_product"),
    path("product_form/", ProductCreateView.as_view(), name="product_form"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/can_unpublish/", CanUnpublishProductView.as_view(), name="can_unpublish_product"),
    path("products/category/<slug:category_slug>/", ProductsByCategoryView.as_view(), name="products_by_category"),
]
