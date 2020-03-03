"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from pages import views
from product.views import home,product_form_view,product_form2_view,product_form_update,product_dinamic_view,product_delete_view,product_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.home),
    path('content/',views.content),
    path('about/',views.about),
    path('base/',views.base),
    path('product/home',home),
    path('product/form',product_form_view),
    path('product/form1',product_form2_view),
    path('product/update/<int:id>/',product_form_update),
    path('product/dynamic/<int:id>/',product_dinamic_view),
    path('product/delete/<int:id>/',product_delete_view),
    path('product/',product_all),
    
]
