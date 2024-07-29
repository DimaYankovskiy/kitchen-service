from django.contrib.auth import views as auth_views
from django.urls import path

from kitchen.views import (
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeListView,
    DishTypeUpdateView,
    DishCreateView,
    DishDeleteView,
    DishDetailedView,
    DishListView,
    DishUpdateView,
    IngredientCreateView,
    IngredientDeleteView,
    IngredientListView,
    IngredientUpdateView,
)

urlpatterns = [
    path("dish-types/", DishTypeListView.as_view(), name="dish_type-list"),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete"
    ),

    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "ingredient/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create"
    ),
    path(
        "ingredient/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update"
    ),
    path(
        "ingredient/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete"
    ),

    path("", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailedView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),


    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]

app_name = "kitchen"
