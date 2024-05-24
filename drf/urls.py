from django.contrib import admin
from django.urls import path, include
# from login import views
# from login.views import RegisterUpdate1
from register.views import username, RegisterUpdate
from address.views import address

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/tasks/', views.TaskListCreate.as_view()),
    # path('api/tasks/<int:pk>', views.TaskDetailUpdateDelete.as_view()),
    path('register/', username.as_view(), name='register-list-create'),
    path('register/<int:pk>/', RegisterUpdate.as_view(), name='register-update'),
    path('address/', address.as_view(), name="Address_user"),
    # path('register/<int:pk>/', RegisterUpdate.as_view(), name='register-update'),

]
