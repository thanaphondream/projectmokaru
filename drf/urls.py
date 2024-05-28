from django.contrib import admin
from django.urls import path, include
from register.views import RegisterListCreate, Rgall
from login.views import LoginView
from address.views import address

urlpatterns = [
    path('admin/', admin.site.urls),
    path('address/', address.as_view(), name="Address_user"),
    path('register/', Rgall.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login')
    
]
