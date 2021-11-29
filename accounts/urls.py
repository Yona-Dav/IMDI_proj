from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile')
]