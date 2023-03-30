from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserProfile, UpdateUserData
from .models import Profile, ShoppingBag
from business_account.models import BusinessAccount, BusinessAccountOrders
from items.models import Item
from django.contrib import messages


@login_required
def profile(request):
    business_account_check = BusinessAccount.objects.filter(owner=request.user)
    return render(request, 'user_profile/profile.html', {"check": business_account_check})


def account_details(request):
    profile_details = Profile.objects.all()
    return render(request, "user_profile/account_details.html", {'profile': profile_details})


def edit_account_details(request):
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

    return render(request, 'user_profile/edit_account_details.html', context)


def shopping_bag(request):
    prices = []
    items = ShoppingBag.objects.filter(buyer=request.user)
    for i in items:
        f = i.item.add_price
        prices.append(f)

    price = sum(prices)

    context = {
        "items": items,
        "price": price,
    }

    return render(request, 'user_profile/shopping_bag.html', context)


def add_to_shopping_bag(request, pk):
    item = Item.objects.get(id=pk)
    buyer = request.user

    added_item = ShoppingBag.objects.create(item_id=item.id, buyer=buyer)
    added_item.save()

    messages.success(request, "Item is added to your shopping bag successfully")
    return redirect("item_view", pk)


def buy(request):
    items = ShoppingBag.objects.filter(buyer=request.user)

    if request.method == "POST":
        for i in items:
            buyer_item_name = f'Name: {i.item.add_name}, Price: {i.item.add_price}'
            bought = BusinessAccountOrders.objects.create(buyer=request.user, buyer_item=buyer_item_name, owner_item=i.item.owner)
            bought.save()

        return redirect('shopping_bag')

    return render(request, 'user_profile/buy.html', {"items": items})


def clear(request):
    items = ShoppingBag.objects.filter(buyer=request.user)
    items.delete()

    return redirect('shopping_bag')


def delete_from_bag(request, pk):
    items = ShoppingBag.objects.get(id=pk)
    items.delete()
    return redirect('shopping_bag')
