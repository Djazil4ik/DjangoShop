from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('product/<str:slug>', views.detail_view, name='detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<str:slug>/', views.Delete_Product, name='delete_product'),
    path('edit_product/<str:slug>/', views.Update_Product, name='edit-product'),
    path('edit_profile/', views.edit_seller_profile, name='edit-profile'),
]