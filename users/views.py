from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from users.forms import CustomUserForm
from users.models import CustomUser


class CustomUserCreateView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "registration/registration.html"
    success_message = "Account created successfully! You can login now."
