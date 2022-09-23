from django.shortcuts import render
from models.models import Model
from brands.models import Brand
# Create your views here.


def brand_cars(request, id):
    brand = Brand.objects.get(id=id)
    models = Model.objects.filter(brand=brand)

    data = {
        'brand': brand,
        'models': models,
    }

    return render(request, 'brand_cars.html', context=data)
