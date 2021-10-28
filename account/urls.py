from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('register/', views.register, name='register'),
    path('profile/<int:uid>', views.profile, name='profile'),
    path('profile/<int:uid>/settings', views.profile_settings, name='settings')
]
