from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns=[
    ## calling a class based view
    path('', views.IndexView.as_view(), name='index'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('musician_detail/<pk>/', views.MusicianDetail.as_view(), name='musician_detail'),
    path('musician_update/<pk>/', views.MusicianUpdate.as_view(), name='musician_update'),
    path('musician_delete/<pk>/', views.MusicianDelete.as_view(), name='musician_delete'),
    ## old def based view
    path('add_album/', views.album_form, name='album_form'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('all_albums/', views.all_albums, name='all_albums'),
    path('all_musicians/', views.all_musicians, name='all_musicians'),
]
