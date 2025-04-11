from django.urls import path
from .views import home_view, register_view, login_view, logout_view, dashboard_view, edit_profile_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('edit/', edit_profile_view, name='edit_profile'),

]
