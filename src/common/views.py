from django.shortcuts import render

# Create your views here.
from framework.views import DefaultFeatures


class UserLogin(DefaultFeatures):
    def action_on_get(self, request, *args, **kwargs):
        pass

    def action_on_post(self, request, *args, **kwargs):
        pass


class UserLogout(DefaultFeatures):
    def action_on_get(self, request, *args, **kwargs):
        pass

    def action_on_post(self, request, *args, **kwargs):
        pass


class UserChangePassword(DefaultFeatures):
    def action_on_get(self, request, *args, **kwargs):
        pass

    def action_on_post(self, request, *args, **kwargs):
        pass
