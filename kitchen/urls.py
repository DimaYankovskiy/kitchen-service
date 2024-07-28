from django.urls import path

from kitchen.views import temporary

path(
    "", temporary, name="temporary"
),

urlpatterns = [
    path("", temporary, name="temporary"),
]

app_name = "kitchen"
