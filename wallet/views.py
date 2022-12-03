from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import WalletForm
from .models import Wallet
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def ret_wallet(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            price = request.POST['price']
            return JsonResponse({
                'success': True,
                'message': "Payment in amount of " + str(price) + " has been sucessfully sent",
                'price': str(price)
                })
        else:
            return JsonResponse({
                'success': False,
                'message': "Payment failed"
                })

