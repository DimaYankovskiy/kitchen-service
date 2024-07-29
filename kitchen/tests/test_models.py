from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Cook, Ingredient, Dish

User = get_user_model()


class DishTypeModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Appetizer")

    def test_dish_type_creation(self):
        self.assertEqual(self.dish_type.name, "Appetizer")
        self.assertTrue(isinstance(self.dish_type, DishType))
        self.assertEqual(str(self.dish_type), "Appetizer")


class CookModelTest(TestCase):
    def setUp(self):
        self.cook = User.objects.create(
            username="chef",
            password="password123",
            years_of_experience=5
        )

    def test_cook_creation(self):
        self.assertEqual(self.cook.username, "chef")
        self.assertEqual(self.cook.years_of_experience, 5)
        self.assertTrue(isinstance(self.cook, Cook))
        self.assertEqual(str(self.cook), "chef")


class IngredientModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="Tomato")

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, "Tomato")
        self.assertTrue(isinstance(self.ingredient, Ingredient))
        self.assertEqual(str(self.ingredient), "Tomato")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = User.objects.create_user(username="chef", password="password123")
        self.ingredient = Ingredient.objects.create(name="Chicken")
        self.dish = Dish.objects.create(
            name="Chicken Curry",
            description="Spicy chicken curry",
            price=12.99,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_dish_creation(self):
        self.assertEqual(self.dish.name, "Chicken Curry")
        self.assertEqual(self.dish.description, "Spicy chicken curry")
        self.assertEqual(self.dish.price, 12.99)
        self.assertEqual(self.dish.dish_type, self.dish_type)
        self.assertIn(self.cook, self.dish.cooks.all())
        self.assertIn(self.ingredient, self.dish.ingredients.all())
        self.assertTrue(isinstance(self.dish, Dish))
        self.assertEqual(str(self.dish), "Chicken Curry")
