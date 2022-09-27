from django.http import HttpResponse
from django.shortcuts import render
from models.models import Model
from brands.models import Brand
from models.models import Series
# Create your views here.


def brand_cars(request, id):
    if Model.objects.count() < id:
        return HttpResponse("error. PAGE NOT FOUND")
    context = {
        'models': Model.objects.all(),
        'brand': Brand.objects.get(id=id)
    }
    return render(request, 'posts.html', context)


def series(request, brand_id, model_id):
    context = {
        'model': Model.objects.get(id=model_id),
        'series': Series.objects.filter()
    }
    return render(request, 'series.html', context)

def series_model_view(request, brand_id, model_id):
    brand = Brand.objects.get(id=brand_id)
    models = Model.objects.get(id=model_id)
    series = Series.objects.filter(serie_one_to_many_for_model_id=models)
    array = {
        'brand': brand,
        'models': models,
        'series': series
    }
    return render(request, 'series.html', context=array)