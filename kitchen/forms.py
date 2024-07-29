from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Dish, DishIngredient


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))


class DishIngredientForm(forms.ModelForm):
    class Meta:
        model = DishIngredient
        fields = ["ingredient", "ingredient_mass"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


DishIngredientFormSet = inlineformset_factory(Dish, DishIngredient, form=DishIngredientForm, extra=1, can_delete=True)
