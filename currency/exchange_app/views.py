from locale import currency
from multiprocessing import context
from django.shortcuts import render

import requests

def exchange(request):
    r = requests.get('https://v6.exchangerate-api.com/v6/8ee949f19c6c280b3dffa366/latest/USD').json()
    currencies = r.get('conversion_rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
    
        return render(request, 'exchange_app/index.html', context=context)

    if request.method == 'POST':
        all_amount = float(request.POST.get('all-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        print(all_amount)

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(all_amount), 2)

        context = {
            'all_amount': all_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'converted_amount': converted_amount,
            'currencies': currencies
        }

        return render(request, 'exchange_app/index.html', context=context)
