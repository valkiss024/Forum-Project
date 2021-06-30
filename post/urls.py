from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("posts/create", views.CreatePostView.as_view(), name="post-create"),
    path("posts/<int:pk_post>/delete", views.DeletePostView.as_view(), name="post-delete")
]
