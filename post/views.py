from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from main_topic.models import MainTopic
from post.models import Post
from sub_topic.models import SubTopic


class PostListView(ListView):

    """A ListView of all the posts belonging to the chosen sub topic"""

    model = Post
    context_object_name = "post_list"
    template_name = "post/post_list_view.html"
    paginate_by = 4

    def get_sub_topic(self, **kwargs):
        """Get the SubTopic object using the object's id from the URL"""
        return get_object_or_404(SubTopic, id=self.kwargs["pk_sub"])

    def get_queryset(self):
        """Update the queryset with only the relevant posts in a reversed order by the date they were created"""
        original_queryset = super().get_queryset()
        return original_queryset.filter(sub_topic=self.get_sub_topic()).order_by("-date")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sub_topic"] = SubTopic.objects.get(id=self.kwargs["pk_sub"])
        context["main_topic"] = MainTopic.objects.get(id=self.kwargs["pk"])
        return context


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    """Create a new post - only authenticated users are able to access it"""

    model = Post
    template_name = "post/post_create_view.html"
    fields = ["title", "content", "image"]
    login_url = "login"
    success_message = "Your post has been added."

    def form_valid(self, form):
        sub_topic = SubTopic.objects.get(id=self.kwargs["pk_sub"])
        form.instance.author = self.request.user
        form.instance.sub_topic = sub_topic
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    """Delete a post - only the admin user is able to access it"""

    model = Post
    context_object_name = "post"
    template_name = "post/post_delete_view.html"

    def get_object(self, queryset=None):
        return Post.objects.get(id=self.kwargs["pk_post"])

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("post-list", args=[self.kwargs["pk"], self.kwargs["pk_sub"]])

    def test_func(self):
        return self.request.user.is_superuser
