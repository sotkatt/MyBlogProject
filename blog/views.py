from django.shortcuts import render, redirect
from blog.models import Baloon, BaloonColor, BaloonSize, BaloonType


def index(request):

    # select * from Baloon
    baloons = Baloon.objects.all()

    context = {
        'all_baloons': baloons
    }

    return render(request, 'index.html', context)


def index_detail(request, pk):
    # select * from Baloon where id = pk
    baloon = Baloon.objects.get(id=pk)

    context = {
        'baloon': baloon
    }

    return render(request, 'index_detail.html', context)