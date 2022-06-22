from django.core import serializers
from django.http import JsonResponse
from product.models import Product, Color, Category, Size
import json


def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_json = serializers.serialize('json', products)
        return JsonResponse(status=200, data=products_json, safe=False)
    elif request.method == 'POST':
        req_body = json.loads(request.body.decode("utf-8"))
        category = req_body["category"]
        sizes = req_body["size"]
        colors = req_body["color"]

        size_arr = sizes.split(',')
        colors_arr = colors.split(',')

        Category.objects.get_or_create(label=category)

        new_product = Product.objects.create(
            name=req_body['name'],
            code=req_body['code'],
            category=Category.objects.get(label=category),
            unit_prize=req_body['unit_prize'],
            inventory=req_body['inventory']
        )

        for size in size_arr:
            Size.objects.get_or_create(label=size)
            new_product.size.add(Size.objects.get(label=size))
        for color in colors_arr:
            Color.objects.get_or_create(label=color)
            new_product.color.add(Color.objects.get(label=color))
        new_product.save()
        products_json = serializers.serialize('json', new_product)
        return JsonResponse(status=200, data=products_json, safe=False)
    else:
        return JsonResponse(status=405, data={"message": "method not allowed"},  safe=False)


def update_product(request, name):
    if request.method == 'PUT':
        # try:
        product = Product.objects.get(name=name)
        req_body = json.loads(request.body.decode("utf-8"))
        category = req_body["category"]
        sizes = req_body["size"]
        colors = req_body["color"]

        size_arr = sizes.split(',')
        colors_arr = colors.split(',')

        Category.objects.get_or_create(label=category)
        new_cate = Category.objects.get(label=category)
        product.code = req_body['code']
        product.category = new_cate,
        product.unit_prize = req_body['unit_prize'],
        product.inventory = req_body['inventory']
        product.size.all().delete()
        product.color.all().delete()
        for size in size_arr:
            Size.objects.get_or_create(label=size)
            product.size.add(Size.objects.get(label=size))
        for color in colors_arr:
            Color.objects.get_or_create(label=color)
            product.color.add(Color.objects.get(label=color))
        product.save()
        products_json = serializers.serialize('json', new_product)
        return JsonResponse(status=200, data=products_json, safe=False)
        # except:
            #return JsonResponse(status=404, data={"message": "not found"}, safe=False)
    else:
        return JsonResponse(status=405, data={"message": "method not allowed"},  safe=False)


def delete_product(request, name):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(name=name)
            product.delete()
            return JsonResponse(status=200, data={"message": "success"}, safe=False)
        except:
            return JsonResponse(status=404, data={"message": "not found"}, safe=False)
    else:
        return JsonResponse(status=405, data={"message": "method not allowed"}, safe=False)

