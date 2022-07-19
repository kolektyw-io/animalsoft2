from django.http import HttpResponse
from django.urls import path

from framework.views import DefaultFeatures, LoginRequiredView


class Home(DefaultFeatures):
    def action_on_get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world")


class Login(DefaultFeatures):
    def action_on_get(self, request, *args, **kwargs):
        pass

    def action_on_post(self, request, *args, **kwargs):
        pass


class Logout(LoginRequiredView):
    def action_on_get(self, request, *args, **kwargs):
        pass

    def action_on_post(self, request, *args, **kwargs):
        pass


urlpatterns = [
    path('', Home.as_view(), name="home")
]
