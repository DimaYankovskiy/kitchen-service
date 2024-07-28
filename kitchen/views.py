from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import DishType, Ingredient


def temporary(request):
    return render(request, "base.html")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"
    success_url = reverse_lazy("kitchen:ingredient-list")
