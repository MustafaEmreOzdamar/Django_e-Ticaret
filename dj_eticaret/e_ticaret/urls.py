from django.urls import path
from . import views
app_name = "e_ticaret"

urlpatterns = [
     path('', views.home, name='home'),
     path('signup/', views.signup_view, name='signup'),
     path('login/',views.login_view, name='login'),
     path('cart/', views.cart_view,name='cart'),
     path('search/',views.search_view,name='search'),
     path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
]
