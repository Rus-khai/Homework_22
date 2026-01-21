from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/detail_product.html"
    context_object_name = "product"


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/catalog_list.html"
    context_object_name = "object_list"
