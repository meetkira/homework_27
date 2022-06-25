import json
import os

from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad, Category


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AddInfo(View):
    def get(self, request):
        try:
            json_files = [os.path.abspath('datasets/ads.json'), os.path.abspath('datasets/categories.json')]

            with open(json_files[0], 'r', encoding='utf-8') as jsonf:
                data = json.loads(jsonf.read())
            for item in data.values():
                ad = Ad()
                ad.name = item["name"]
                ad.author = item["author"]
                ad.description = item.get("description", None)
                ad.price = int(item["price"])
                ad.address = item["address"]
                ad.is_published = bool(item["is_published"])

                ad.save()

            with open(json_files[1], 'r', encoding='utf-8') as jsonf:
                data = json.loads(jsonf.read())
            for item in data.values():
                cat = Category()
                cat.name = item["name"]
                cat.save()

            return HttpResponse("Данные успешно выгружены", status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        responce = []
        for ad in ads:
            responce.append({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })

        return JsonResponse(responce, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        try:
            ad = Ad()
            ad.name = ad_data["name"]
            ad.author = ad_data["author"]
            ad.description = ad_data.get("description", None)
            ad.price = int(ad_data["price"])
            ad.address = ad_data["address"]
            ad.is_published = bool(ad_data["is_published"])

            ad.save()

            return JsonResponse({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            }, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=403)
