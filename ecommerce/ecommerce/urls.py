"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('register_data/',views.register_data,name='register_data'),
    path('login_data/',views.login_data,name='login_data'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('add_product/',views.add_product,name='add_product'),
    path('view_products/',views.view_products,name='view_products'),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    path('view_users/',views.view_users,name='view_users'),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/add/<int:id>/',views.cart_add,name='cart_add'),
    path('cart/',views.cart,name='cart'),
    path('remove/cart/<int:id>/',views.remove_cart,name='remove_cart'),
    path('cart/delete/<int:id>/',views.cart_delete,name='cart_delete'),
    path('checkout/',views.checkout,name='checkout'),
    path('place_order/',views.place_order,name='place_order'),
    path('order/history/',views.order_history,name='order_history'),
    path('logout/',views.logout,name='logout'),

]


