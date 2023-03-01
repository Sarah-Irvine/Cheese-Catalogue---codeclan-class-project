from django.shortcuts import render, get_object_or_404
from .models import Cheese, Review

# Create your views here.
def home(request):

    query_params = request.GET

    filter_map = {
        "query": "name__icontains",
        "strength": "strength",
        "country": "country__iexact"
    }

    # one way to search:
    # if "query" in query_params:
    #     cheese_name_query = query_params["query"]
    #     cheese_strength_query = query_params["strength"]
    #     cheese_query = Cheese.objects.filter(name__icontains=cheese_name_query, strength=int(cheese_strength_query))
    # else:
    #     cheese_query = Cheese.objects.all()

    filters = {}
    for key, value in query_params.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    cheeses = Cheese.objects.filter(**filters)


    context = {
        "cheeses": cheeses
    }

    #"reviews": Review.objects.filter(recommend=True) 
    #passed into context would give us all the cheeses, filter the reviews. Can filter on any of your attributes
    return render(request,'catalogue/home.html', context)

def cheese_details(request, id):

    context = {
        "cheese": get_object_or_404(Cheese, id=id)
    }

    return render(request, "catalogue/cheese_details.html", context)