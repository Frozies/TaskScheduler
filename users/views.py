from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from .forms import UserDeactivateForm, UserDeleteForm


class UserDeactivateView(LoginRequiredMixin, View):
    """
    Deactivates the currently signed-in user by setting is_active to False.
    """

    def get(self, request, *args, **kwargs):
        form = UserDeactivateForm()
        return render(request, 'user_deactivation.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDeactivateForm(request.POST)
        # Form will be valid if checkbox is checked.
        if form.is_valid():
            # Make user inactive and save to database.
            request.user.is_active = False
            request.user.save()
            # Log user out.
            logout(request)
            # Give them a success message.
            messages.success(request, 'Account successfully deactivated')
            # Redirect to home page.
            return redirect(reverse('home'))
        return render(request, 'user_deactivation.html', {'form': form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, 'user_deletion.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        # Form will be valid if checkbox is checked.
        if form.is_valid():
            user = request.user
            # Logout before we delete. This will make request.user
            # unavailable (or actually, it points to AnonymousUser).
            logout(request)
            # Delete user (and any associated ForeignKeys, according to
            # on_delete parameters).
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect(reverse('home'))
        return render(request, 'user_deletion.html', {'form': form})
