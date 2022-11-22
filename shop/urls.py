from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
     #path('', views.category, name='category'),
     path('shop/', views.allProdCat, name='products_by_category'),
     #path('index/', views.categorydetail, name='category'),
     path('shop/<int:Product_id>/', views.productdetail, name='productdetail'),
     path('delete/<int:product_id>/', views.delete, name='delete'),
     path('shop/category/<int:category_id>', views.categorydetail),
     path('product/create/', views.product_create, name='product_create'),




]
