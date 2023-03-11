from django.shortcuts import render, get_object_or_404, redirect
from .models import Cheese, Review, Customer
from .forms import CheeseForm

# Create your views here.
def home(request):

    query_params = request.GET

    filter_map = {
        "query": "name__icontains",
        "strength": "strength",
        "colour": "colour__icontains",
        "country": "country__iexact",
        "age": "age__iexact"
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

    countries = Cheese.objects.values_list("country", flat=True).distinct()
    
    if request.method == "POST":
        form = CheeseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            print(name)
    else:
        form = CheeseForm()

    context = {
        "cheeses": cheeses,
        "countries": countries,
        "form": form
    }

    #"reviews": Review.objects.filter(recommend=True) 
    #passed into context would give us all the cheeses, filter the reviews. Can filter on any of your attributes
    return render(request,'catalogue/home.html', context)

def cheese_details(request, id):

    context = {
        "cheese": get_object_or_404(Cheese, id=id)
    }

    return render(request, "catalogue/cheese_details.html", context)


def customer(request, id):
    context = {
        "customer": get_object_or_404(Customer, id=id)
    }
    return render(request, "catalogue/customer.html", context)

def add_review(request, id):
    if request.method =="POST":
        customer = get_object_or_404(Customer, id=id)
        cheese = request.POST.get("cheese")
        cheese_obj = get_object_or_404(Cheese, id=int(cheese))
        recommend = True
        rating = request.POST.get("rating")
        review = Review(reviewer=customer, cheese=cheese_obj, rating=int(rating), recommend=recommend)
        review.save()
        return redirect(request.POST.get("redirect_url"))

def add_cheese(request):
    if request.method == "POST":
        name = request.POST.get("name")
        strength = request.POST.get("strength")
        colour = request.POST.get("colour")
        country = request.POST.get("country")
        age = request.POST.get("age")

        cheese = Cheese(name=name, strength=int(strength), colour=colour, country=country, age=int(age))
        cheese.save()
        return redirect(request.POST.get("redirect_url"))
