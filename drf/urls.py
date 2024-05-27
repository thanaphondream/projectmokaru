from django.contrib import admin
from django.urls import path, include
# from login import views
# from login.views import RegisterUpdate1
from login.views import RegisterView, LoginView, UserDetailView, UsersGet
# from register.views import username, RegisterUpdate, UserRegistration, UserLogin
from register.views import RgListCreate, LoginView1
from address.views import address

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/tasks/', views.TaskListCreate.as_view()),
    # path('api/tasks/<int:pk>', views.TaskDetailUpdateDelete.as_view()),
    # path('register/', username.as_view(), name='register-list-create'),
    # path('register/<int:pk>/', RegisterUpdate.as_view(), name='register-update'),
    path('address/', address.as_view(), name="Address_user"),
    # path('register/<int:pk>/', RegisterUpdate.as_view(), name='register-update'),
    path('registers/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<str:email>/', UserDetailView.as_view(), name='user-detail'),
    path('userget/', UsersGet.as_view()),
    path('register1s/', RgListCreate.as_view()),
    path('logins01/',LoginView1.as_view(), name='login'),
    

]
