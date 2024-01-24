from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.index,name="index"),
    path('register/chatmate/',views.register,name="register"),
]
