from django.urls import path, include
from main_topic import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("main-categories", views.MainTopicListView.as_view(), name="main-topic-list"),
    path("main-categories/create", views.CreateMainTopicView.as_view(), name="main-topic-create"),
    path("main-categories/<int:pk>/update", views.UpdateMainTopicView.as_view(), name="main-topic-update"),
    path("main-categories/<int:pk>/delete", views.DeleteMainTopicView.as_view(), name="main-topic-delete"),
    path("main-categories/<int:pk>/", include("sub_topic.urls"))
]
