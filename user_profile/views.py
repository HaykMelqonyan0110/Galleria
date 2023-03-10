from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserProfile, UpdateUserData
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def profile(request):
    if request.method == "POST":
        d_form = UpdateUserData(request.POST, instance=request.user)
        p_form = UpdateUserProfile(request.POST, request.FILES, instance=request.user.profile)

        if d_form.is_valid() and p_form.is_valid():
            d_form.save()
            p_form.save()

    else:
        d_form = UpdateUserData(instance=request.user)
        p_form = UpdateUserProfile(instance=request.user.profile)

    context = {
        "d_form": d_form,
        "p_form": p_form
    }

    return render(request, 'user_profile/profile.html', context)


def account_details(request):
    return render(request, "user_profile/account_details.html")


def edit_account_details(request):
    return render(request, "user_profile/edit_account_details.html")


def returns(request):
    return render(request, "user_profile/returns.html")






