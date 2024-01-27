from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.index,name="index"),
    path('register/chatmate/',views.register,name="register"),
    path('ChatMate/friend_find/',views.friend_find,name="friend_find"),
    path('ChatMate/friend_finds/',views.send_details,name="send_details"),
]
