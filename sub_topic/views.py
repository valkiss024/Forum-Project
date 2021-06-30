from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, CreateView

from main_topic.models import MainTopic
from sub_topic.models import SubTopic


class SubTopicListView(ListView):

    """A listview for all the subtopics belonging to the chosen main topic"""

    model = SubTopic
    context_object_name = "sub_topic_list"
    template_name = "sub_topic/sub_topic_list_view.html"

    def get_main_topic(self, **kwargs):
        """Fetch the corresponding main topic object using the 'title' parameter from the URL"""
        return get_object_or_404(MainTopic, id=self.kwargs.get("pk"))

    def get_queryset(self):
        """Update the queryset with a filter query to get only the sub topics which belong to the chosen main topic,
        ordered by the date it was created in a reverse order"""
        original_queryset = super().get_queryset()
        return original_queryset.filter(main_topic=self.get_main_topic()).order_by("-date")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Update template context to access the main topic from the 'sub_topic_list_view' template"""
        context = super().get_context_data(**kwargs)
        context["main_topic"] = self.get_main_topic()
        return context


class CreateSubTopicView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    """Create a new sub topic - only logged in users are able to access it"""

    model = SubTopic
    template_name = "sub_topic/sub_topic_create_view.html"
    fields = ["title", "description"]
    login_url = "login"
    success_message = "Topic has been created successfully"

    def form_valid(self, form):
        main_topic = MainTopic.objects.get(id=self.kwargs["pk"])
        form.instance.author = self.request.user
        form.instance.main_topic = main_topic
        return super().form_valid(form)


class UpdateSubTopicView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):

    """Update an existing sub topic - only the admin and the author of the topic able to access it"""

    model = SubTopic
    template_name = "sub_topic/sub_topic_update_view.html"
    fields = ["title", "description"]
    login_url = "login"
    success_message = "Topic has been updated!"

    def get_object(self, queryset=None):
        print(self.kwargs["pk_sub"])
        return SubTopic.objects.get(id=self.kwargs["pk_sub"])

    def test_func(self):
        """Overwriting UserPassesTestMixin's test_func method"""
        sub_topic_obj = self.get_object()
        return self.request.user.is_superuser or sub_topic_obj.author == self.request.user


class DeleteSubTopicView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    """Delete a sub topic - only the admin is able to access it"""

    model = SubTopic
    context_object_name = "sub_topic"
    template_name = "sub_topic/sub_topic_delete_view.html"
    login_url = "login"

    def get_object(self, queryset=None):
        return SubTopic.objects.get(id=self.kwargs["pk_sub"])

    def get_success_url(self, *args, **kwargs):
        """The URL where the user will be redirected upon success"""
        return reverse_lazy("sub-topic-list", args=[self.kwargs["pk"]])

    def test_func(self):
        """Overwriting UserPassesTestMixin's test_func method"""
        return self.request.user.is_superuser
