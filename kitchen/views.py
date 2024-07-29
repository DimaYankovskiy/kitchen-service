from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import DishType, Ingredient, Dish


def index(request):
    return render(request, "base.html")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"
    success_url = reverse_lazy("kitchen:ingredient-list")


class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDetailedView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    success_url = reverse_lazy("kitchen:dish-detail")
    queryset = (Dish
                .objects.select_related("dish_type")
                .prefetch_related("cooks", "ingredients"))


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"
