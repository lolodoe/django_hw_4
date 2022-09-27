from django.shortcuts import render
from brands.models import Brand
# Create your views here.


def main(request):
    brands = Brand.objects.all()

    data = {
        'brands': brands,
    }

    return render(request, 'brand_cars.html', context=data)
