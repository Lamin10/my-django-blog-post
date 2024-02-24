from django.urls import path
from .views import index, register, login, logout

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # Other URL patterns for other views...
]