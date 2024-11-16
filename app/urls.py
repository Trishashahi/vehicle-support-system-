from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path('comments/', views.comments, name='comments'),
    path('cart/', views.cart, name='cart'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('showroom_near_me/', views.showroom_near_me, name='showroom_near_me'),
    path('need_repair/', views.need_repair, name='need_repair'),
    path('details/', views.details_view, name='details'),
    path('login/', views.login_view, name='login'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('signup/', views.signup_view, name='signup'),
    path('place_order/', views.place_order, name='place_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkoutbtn/', views.checkoutbtn, name='checkoutbtn'),
    path('logout/', views.logout_view, name='logout'),
]
