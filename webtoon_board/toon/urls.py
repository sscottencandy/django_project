from django.urls import path
from . import views

app_name = 'toon'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:toon_id>', views.toon_detail, name='detail'),
    #path('write', views.toon_create, name='create'),
    path('<int:comment_id>/edit', views.toon_edit, name='edit'),
    path('<int:comment_id>/delete', views.toon_delete, name='delete'),
]