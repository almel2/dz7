from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import UserForm


def index(request):
    return HttpResponse("<h1>Для расчета гипотенузы перейдите на 'triangl/'</h1>")


def triangle(request):
    if request.method == "GET":
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            kat1 = form.cleaned_data['kat1']
            kat2 = form.cleaned_data['kat2']
            result = (kat1 ** 2 + kat2 ** 2) ** 0.5
            return HttpResponse(f'Катет равен {result}')

    return render(request, "polls/index.html", context={"form": form})
