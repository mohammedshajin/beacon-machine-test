from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'product/product.html', context)

@login_required
def wishlist_add(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.wishlist.filter(id=request.user.id).exists():
        product.wishlist.remove(request.user)
    else:
        product.wishlist.add(request.user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def wishlist(request):
    products = Product.objects.filter(wishlist=request.user)
    context = {"products":products}
    return render(request, 'product/wishlist.html', context)
