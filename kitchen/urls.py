from django.urls import path
from django.contrib.auth import views as auth_views

from kitchen.views import temporary, DishTypeListView, IngredientListView

urlpatterns = [
    path("", temporary, name="temporary"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

app_name = "kitchen"
