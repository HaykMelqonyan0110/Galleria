from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView
from .forms import ItemForm
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def add_item(request):
    print()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()

            return redirect('bs_account_details')
        else:
            print(form.errors)
    else:
        form = ItemForm()

    return render(request, 'items/add_item.html', {"form": form})


class OwnerItem(DetailView):
    model = Item
    template_name = 'items/owner_item_view.html'


class ItemUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = 'items/update_item.html'
    fields = [
        'add_name',
        'add_price',
        'add_material',
        'add_main_category',
        'add_subcategory',
        'add_description',
        'add_color',
        'add_shoes_size',
        'add_clothing_size',
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.add_image = self.request.FILES.get('add_image')
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.owner:
            return True
        return False


class ItemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/business/account_details/'
    template_name = 'items/delete_item.html'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.owner:
            return True
        return False
