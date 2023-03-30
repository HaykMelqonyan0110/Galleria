from django.shortcuts import render
from items.models import Item
from django.views.generic import DetailView
from business_account.models import BusinessAccount


def home_page_view(request):
    company = BusinessAccount.objects.all()
    items = Item.objects.filter()
    context = {
        'company': company,
        "items": items,
    }

    return render(request, 'homepage/home.html', context)


def men_shop_view(request):
    items = Item.objects.filter(add_main_category='men')

    context = {
        "items": items,
    }
    return render(request, 'homepage/shop_men.html', context)


def men_sub_shop_view(request, subcategory):
    items = Item.objects.filter(add_main_category='men', add_subcategory=subcategory)
    context = {
        "subcategory": subcategory,
        "items": items,
    }

    return render(request, 'homepage/shop_men.html', context)


def women_shop_view(request):
    items = Item.objects.filter(add_main_category='women')

    context = {
        "items": items,
    }
    return render(request, 'homepage/shop_women.html', context)


def women_sub_shop_view(request, subcategory):
    items = Item.objects.filter(add_main_category='women', add_subcategory=subcategory)
    context = {
        "subcategory": subcategory,
        "items": items,
    }

    return render(request, 'homepage/shop_women.html', context)


def kids_shop_view(request):
    items = Item.objects.filter(add_main_category='kids')

    context = {
        "items": items,
    }
    return render(request, 'homepage/shop_kids.html', context)


def kids_sub_shop_view(request, subcategory):
    items = Item.objects.filter(add_main_category='kids', add_subcategory=subcategory)
    context = {
        "subcategory": subcategory,
        "items": items,
    }

    return render(request, 'homepage/shop_kids.html', context)


def subcategory_shop_view(request, subcategory):
    items = Item.objects.filter(add_subcategory=subcategory)
    context = {
        "subcategory": subcategory,
        "items": items,
    }

    return render(request, 'homepage/shop_sub.html', context)


class ItemView(DetailView):
    model = Item
    template_name = 'items/item_view.html'




