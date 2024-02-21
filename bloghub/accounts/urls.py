from django.urls import path

from . import views

app_name="accounts"
urlpatterns = [
    
    path("",views.login_user, name='login_it'),
    path('user_register/', views.add_user, name='register_now'),
    path('logout/', views.logout_user, name='logout'),

]