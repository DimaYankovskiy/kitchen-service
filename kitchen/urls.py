from django.urls import path

from kitchen.views import temporary, DishTypeListView, IngredientListView

urlpatterns = [
    path("", temporary, name="temporary"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
]

app_name = "kitchen"
