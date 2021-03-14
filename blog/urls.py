from django.contrib import admin
from django.urls import path

from blog import views
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us' ),
    path('detail/<int:post_id>', views.post_detail, name='detail' ),
    path('new_posts/', PostCreateView.as_view(), name='new_posts' ),
    path('edit_post/', views.edit_post, name='edit_post' ),
    path('detail/<slug:pk>/update', PostUpdateView.as_view(), name='post-update' ),
    path('detail/<slug:pk>/delete', PostDeleteView.as_view(), name='post-delete' ),
]
