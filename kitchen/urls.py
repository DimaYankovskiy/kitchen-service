from django.urls import path
from django.contrib.auth import views as auth_views

from kitchen.views import index, DishTypeListView, IngredientListView, DishListView, DishDetailedView

urlpatterns = [
    # path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailedView.as_view(), name="dish-detail"),


    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

app_name = "kitchen"
