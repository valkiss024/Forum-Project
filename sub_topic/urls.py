from django.urls import path, include
from . import views

urlpatterns = [
    path("sub-categories", views.SubTopicListView.as_view(), name="sub-topic-list"),
    path("sub-categories/create", views.CreateSubTopicView.as_view(), name="sub-topic-create"),
    path("sub-categories/<int:pk_sub>/update", views.UpdateSubTopicView.as_view(), name="sub-topic-update"),
    path("sub-categories/<int:pk_sub>/delete", views.DeleteSubTopicView.as_view(), name="sub-topic-delete"),
    path("sub-categories/<int:pk_sub>/", include("post.urls"))
]
