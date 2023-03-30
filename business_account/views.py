from django.shortcuts import render, redirect
from items.models import Item
from .forms import RegisterForBusinessAccount, UpdateAccountData, UpdateAccountImage
from .models import BusinessAccount, BusinessAccountOrders


def business_account_views(request):
    account_name = BusinessAccount.objects.filter(owner=request.user)
    return render(request, 'business_account/business_account.html', {"name": account_name})


def register_business_account_view(request):
    if request.method == 'POST':
        form = RegisterForBusinessAccount(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()

            return redirect('business_account')
        else:
            print(form.errors)
    else:
        form = RegisterForBusinessAccount()

    return render(request, 'business_account/register_for_business_account.html', {"form": form})


def edit_business_account_view(request):
    bs_account_image = BusinessAccount.objects.filter(owner=request.user)
    if request.method == "POST":
        d_form = UpdateAccountData(request.POST, instance=request.user.businessaccount)
        p_form = UpdateAccountImage(request.POST, request.FILES, instance=request.user.businessaccount)

        if d_form.is_valid() and p_form.is_valid():
            d_form.save()
            p_form.save()

    else:
        d_form = UpdateAccountData(instance=request.user.businessaccount)
        p_form = UpdateAccountImage(instance=request.user.businessaccount)

    context = {
        "d_form": d_form,
        "p_form": p_form,
        "image": bs_account_image,
    }
    return render(request, 'business_account/edit_business_profile.html', context)


def business_profile_details_view(request):
    user_items = Item.objects.filter(owner=request.user)
    account = BusinessAccount.objects.get(owner=request.user)

    context = {
        "items": user_items,
        "account": account,
    }
    return render(request, 'business_account/business_profile_details.html', context)


def business_account_orders_view(request):
    orders = BusinessAccountOrders.objects.filter(owner_item=request.user)
    return render(request, 'business_account/business_account_orders.html', {"orders": orders})


def business_account_order_delete(request, pk):
    items = BusinessAccountOrders.objects.get(id=pk)
    items.delete()
    return redirect('bs_account_orders')
