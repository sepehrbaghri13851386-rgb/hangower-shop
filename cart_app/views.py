from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.contenttypes.models import ContentType

from shop_app.models import Shop
from acastori_app.models import acstori# آدرس اپ acstori رو با آدرس واقعی پروژه‌ات جایگزین کن

from .models import Cart, CartItem


# نگاشت اسم رشته‌ای که توی URL/تمپلیت می‌فرستیم، به مدل واقعی
MODEL_MAP = {
    'shop': Shop,
    'acstori': acstori,
}


def get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart


def add_to_cart(request, model_name, product_id):
    model = MODEL_MAP.get(model_name)
    if model is None:
        raise Http404("نوع محصول نامعتبر است")

    product = get_object_or_404(model, id=product_id)
    cart = get_or_create_cart(request)
    content_type = ContentType.objects.get_for_model(model)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=product.id,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')


def cart_detail(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()
    return render(request, 'cart/cart.html', {
        'cart': cart,
        'items': items,
    })