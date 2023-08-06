from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('addactivity/',views.addactivity,name='addactivity'),
    path('donelist/',views.donelist,name='donelist'),
    path('rateus/',views.rateus,name="rateus"),
    path('accounts/register/',views.register,name="register"),
    path('accounts/login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('delete/<int:item_id>',views.delete_item,name="delete_item"),
    path('additemdone/<int:item_id>',views.additemdone,name="additemdone"),
    path('additemhome/<int:item_id>',views.additemhome,name="additemhome"),
    path('delete_done/<int:item_id>',views.delete_item_done,name="delete_item_done")
]
