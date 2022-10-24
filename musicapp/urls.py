from django.urls import path
from .views import SongAPIView, ArtisteAPIView


urlpatterns = [
	path('artiste/list/', ArtisteAPIView.as_view(), name='artiste_list'),
	path('artiste/<int:pk>/', ArtisteAPIView.as_view(), name='artiste'),
	path('song/list/', SongAPIView.as_view(), name='song_list'),
	path('song/<int:pk>/', SongAPIView.as_view(), name='song'),
	path('song/create/', SongAPIView.as_view(), name='song_create'),
	path('song/update/<int:pk>/', SongAPIView.as_view(), name='song_update'),
	path('song/delete/<int:pk>/', SongAPIView.as_view(), name='song_delete'),
]