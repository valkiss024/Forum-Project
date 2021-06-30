from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, TemplateView

from main_topic.models import MainTopic


class HomeView(TemplateView):

    """A TemplateView to render the landing / home page"""

    model = MainTopic
    template_name = "main_topic/home.html"

    def get_context_data(self, **kwargs):
        """Update template context with the three most relevant main topics"""
        context = super().get_context_data(**kwargs)
        context["main_topics"] = MainTopic.objects.all().order_by("-date")[:3]
        return context


class MainTopicListView(ListView):

    """A ListView for all the main topics"""

    model = MainTopic
    context_object_name = "main_topic_list"
    template_name = "main_topic/main_topic_list_view.html"

    def get_queryset(self):
        original_queryset = super().get_queryset()
        return original_queryset.order_by("-date")


class CreateMainTopicView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    """Create a new main topic - only the admin is able to access"""

    model = MainTopic
    template_name = "main_topic/main_topic_create_view.html"
    fields = ["title", "description"]
    login_url = "login"

    def test_func(self):
        return self.request.user.is_superuser


class UpdateMainTopicView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    """Update an existing main topic - only the admin is able to access"""

    model = MainTopic
    template_name = "main_topic/main_topic_update_view.html"
    fields = ["title", "description"]
    login_url = "login"

    def test_func(self):
        return self.request.user.is_superuser


class DeleteMainTopicView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    """Delete an existing main topic - only the admin is able to access"""

    model = MainTopic
    context_object_name = "main_topic"
    template_name = "main_topic/main_topic_delete_view.html"
    login_url = "login"
    success_url = reverse_lazy("main-topic-list")

    def test_func(self):
        return self.request.user.is_superuser
