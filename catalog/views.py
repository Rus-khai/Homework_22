from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        massage = request.POST.get('massage')

        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
    return render(request, 'catalog/contacts.html')
