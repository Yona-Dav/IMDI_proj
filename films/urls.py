from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage/', views.FilmListView.as_view(), name='homepage'),
    path('addFilm/', views.FilmCreateView.as_view(), name='add_film'),
    path('editFilm/<int:pk>/', views.FilmUpdateView.as_view(), name='edit_film'),
    path('addDirector/', views.DirectorCreateView.as_view(), name='add_director'),
    path('editDirector/<int:pk>/', views.DirectorUpdateView.as_view(), name='edit_director'),
    path('<int:pk>/delete/', views.FilmDeleteView.as_view(), name='delete'),
    path('details/<int:film_id>/', views.CommentCreateView.as_view(), name='comment' ),
    path('rating/<int:film_id>/', views.RatingCreateView.as_view(), name='rate' ),

]
