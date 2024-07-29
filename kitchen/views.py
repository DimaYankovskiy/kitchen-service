from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import DishType, Ingredient, Dish


def index(request):
    return render(request, "base.html")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")
    template_name = "kitchen/dishtype_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")
    template_name = "kitchen/dishtype_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish_type-list")
    template_name = "kitchen/dishtype_confirm_delete.html"


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_confirm_delete.html"


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


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/dish_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "kitchen:dish-detail",
            kwargs={"pk": self.object.pk}
        )


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_confirm_delete.html"
