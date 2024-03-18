from django.urls import path
from . import views

urlpatterns = [
    # Páginas de Visualização de tópicos
    path('', views.topic_view, name="topic_view"),
    # Páginas de Cadastrar Post
    path('forum/new_post/', views.new_post, name="new_post"),
    # Página de Comentários 
    path('forum/comment/<int:topic_id>/', views.comment, name='comment'),
    # Página de Editar Post
    path('forum/edit_post/<int:post_id>/', views.edit_post, name="edit_post"),
    # Página de Deleta Post
    path('forum/delete_post/<int:post_id>/', views.delete_post, name="delete_post"),
]