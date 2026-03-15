from django import forms
from catalog.models import Product
from config import settings


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'can_unpublish_product']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите имя'})
        self.fields['price'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Введите цену'})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
                                                        'placeholder': 'Введите описание'})
        self.fields['category'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Введите категорию'})
        self.fields['can_unpublish_product'].widget.attrs.update({'class': 'form-check-input'})

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной.")
        return price

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        forbidden_words = settings.FORBIDDEN_WORDS

        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"В названии обнаружено запрещенное слово '{word}'")

        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        forbidden_words = settings.FORBIDDEN_WORDS

        for word in forbidden_words:
            if word in description:
                raise forms.ValidationError(f"В описании обнаружено запрещенное слово '{word}'")

        return description
