from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('login/', views.SellerLoginView.as_view(), name='login'),
    path('signup/', views.SignUpPage.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile')
]