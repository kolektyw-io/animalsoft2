from django.contrib.auth.models import Group, User
from django.http import HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse


class DefaultFeatures(View):
    """Base Class for views. It supports automatic input for context to identify sessions."""
    get_template = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request: HttpRequest, *args: list, **kwargs: dict) -> HttpResponse:
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:
            HttpResponse object that is suitable for rendering.

        Raises:


        """
        self.prepare_context()
        self.context['user'] = self.request.user
        return self.action_on_get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        self.prepare_context()
        self.context['user'] = self.request.user
        return self.action_on_post(request, *args, **kwargs)

    def action_on_get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        return render(self.request, self.get_template, self.context)

    def action_on_post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented

    def prepare_context(self):
        """
        Creates empty context, suitable for rendering.
        Descendants of the class may alter this behavior, i.e. for putting into
        context dict other features - user data.

        Returns:
            Returns empty context.
        """
        self.context = {}


class ErrorView(DefaultFeatures):
    pass


class LoginRequiredView(DefaultFeatures):
    def get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        if request.user is not None:
            return self.action_on_get(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        if request.user is not None:
            return self.action_on_post(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def not_authorized(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented


class StaffRequiredView(LoginRequiredView):
    """Subclass this view so your class-based view will require staff permissions."""

    def get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        if request.user.is_staff:

            return self.action_on_get(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        if request.user.is_staff:
            return self.action_on_post(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def not_authorized(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented


class SuperuserRequiredView(LoginRequiredView):

    def get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        if request.user.is_superuser:
            return self.action_on_get(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        if request.user.is_superuser:
            return self.action_on_post(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def not_authorized(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented


def is_member(user: User, group: str) -> bool:
    """

    Args:
        user ():
        group ():

    Returns:

    """
    return user.groups.filter(name=group).exists() or user.is_staff


class GroupRequiredView(LoginRequiredView):
    group_name = "DEFAULT_READ"
    group_name_write = "DEFAULT_WRITE"
    get_template = ""
    post_template = ""

    def action_on_get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        return render(self.request, self.get_template, self.context)

    def prepare_context(self):
        """

        Returns:

        """
        pass

    def prepare_context_post(self):
        self.prepare_context()

    def get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        Group.objects.get_or_create(name=self.group_name)
        if is_member(request.user, self.group_name) or request.user.is_staff:
            self.prepare_context()
            return self.action_on_get(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        Group.objects.get_or_create(name=self.group_name_write)
        if is_member(request.user,
                     self.group_name_write) or request.user.is_staff:
            self.prepare_context_post()
            return self.action_on_post(request, *args, **kwargs)
        else:
            return self.not_authorized(self.request, *args, **kwargs)

    def not_authorized(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        self.context["group_lack_right"] = self.group_name
        return render(request,
                      template_name="lack_right.html",
                      context=self.context)


class ConfirmationView(GroupRequiredView):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class APIView(View):
    def get(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented

    def post(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented

    def put(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented

    def delete(self, request, *args, **kwargs):
        """

        Args:
            request ():
            *args ():
            **kwargs ():

        Returns:

        """
        raise NotImplemented
