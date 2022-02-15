from atexit import register
from itertools import product
from django.shortcuts import redirect, render
from .forms import CustomerCreationForm
from django.contrib.auth import authenticate, login, logout

from product.models import Product

def register(request):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')

    context = {"form": form}

    return render(request, 'user/signup.html', context)


# def wishlist(request, pk):
#     product=Product.object.get(id=pk)
#     wishlist = Wishlist.objects.create(user=request.user, product=product)
    
