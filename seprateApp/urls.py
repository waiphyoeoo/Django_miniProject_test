"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name='dashboard'),
    path('customers/<int:id>',views.customers,name='customers.show'),
    path('customer_profile/',views.customer_profile,name='customers.customer_profile'),
    path('customer_profile/setting',views.customer_profile_setting,name='customers.customer_profile_setting'),
    path('products/',views.products,name='products'),
    path('order/create/',views.orderCreate,name='ordercreate'),
    path('order/create/<int:customerId>',views.placeordersCreate,name='placeorderscreate'),
    path('order/update/<int:orderId>',views.orderUpdate,name='orderupdate'),
    path('order/delete/<int:orderId>',views.orderDelete,name='orderdelete'),
    path('register/',views.register,name='register'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),

]