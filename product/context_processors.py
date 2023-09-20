from product.models import ShopDetail



def shop_detail(request):
    shop_detail = ShopDetail.objects.get(pk=1)


    return { 'shop_detail' : shop_detail}