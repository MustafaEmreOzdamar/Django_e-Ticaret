from django.shortcuts import render, redirect ,get_object_or_404
from .models import Product ,Cart
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate , login
 


def home(request):
    products = Product.objects.all()
    return render(request , 'e_ticaret/home.html',{'products':products})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse='login')
    else:
        form = UserCreationForm()
    return render(request , 'e_ticaret/signup.html', {'form' :form})   

def login_view(request):
    if request.method == 'POST':
        username = request.POST[username]
        password = request.POST[password]
        user = authenticate(request , username==username , password==password)
        if user is not None: 
            login(request, user)
            return redirect(reverse('home'))
    return render(request , 'e_ticaret/login.html')

def search_view(request):
    query = request.GET.get('q','')
    products = Product.objects.filter(name__icontains=query)
    return render(request , 'e_ticaret/search.html', {'products' : products , 'query' : query})

def cart_view(request):
    return render(request , 'e_ticaret/cart.html')

@login_required
def add_to_cart(request , product_id):
    product = get_object_or_404(Product, id=product_id)
    
    cart , created = Cart.objects.get_or_create(user = request.user , active=True)
    cart.products.add(product)
    return redirect('e_ticaret:cart')