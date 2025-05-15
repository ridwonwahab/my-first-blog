from django.urls import path
from .import views

#url configuration

urlpatterns = [
    path('home/', views.post_list, name='post_list'),
    path('index/', views.index, name='index'),
    path('shop_detail/', views.shopDeatil, name='shopDetail'),
    path('shop_listing/', views.shopListing, name='listing'),


    path('shout_out/', views.shout_out)
]