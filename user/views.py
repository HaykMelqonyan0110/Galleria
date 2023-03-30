from django.shortcuts import render
from .forms import Registration
from django.shortcuts import redirect


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = Registration()

    return render(request, 'user/register.html', {"form": form})


