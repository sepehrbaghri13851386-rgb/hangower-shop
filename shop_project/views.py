from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import models
from shop_app.models import Shop
from acastori_app.models import acstori
from kharid_app.models import kharid


def home(request):
    shopes = Shop.objects.all().order_by('-id')[:5]
    acstories = acstori.objects.all()
    return render(request, 'index.html', {'shopes': shopes, 'acstori': acstories})


def shop(request):
    query = request.GET.get('q', '').strip()
    kharides_qs = kharid.objects.all()
    if query:
        kharides_qs = kharides_qs.filter(
            models.Q(title__icontains=query) | models.Q(discribshen__icontains=query)
        )
    kharides = list(kharides_qs)
    kharid_pages = [kharides[i:i + 8] for i in range(0, len(kharides), 8)]
    return render(request, 'shop.html', {'kharid': kharides, 'kharid_pages': kharid_pages, 'query': query})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def Nike(request):
    nikes = Shop.objects.filter(category='nike')
    top_liked = Shop.objects.filter(category='nike', likes__gt=0).order_by('-likes')[:5]
    return render(request, 'nike.html', {"nikes": nikes, "top_liked": top_liked})


def Acstori(request):
    acstories = acstori.objects.all()
    return render(request, 'index.html', {'shopes': Shop.objects.all(), 'acstori': acstories})


@require_POST
def like_product(request, pk):
    product = get_object_or_404(Shop, pk=pk)
    product.likes += 1
    product.save()
    return JsonResponse({'likes': product.likes})