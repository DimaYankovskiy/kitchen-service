# Restaurant Kitchen Service

Application for managing kitchen dishes

## Check it out!

[Kitchen service deployed to Render](https://kitchen-service-r1x3.onrender.com/)

Test user <br />
Username: admin <br />
Password: 1qazcde3

## Installation

Python3 must be already installed

```shell
git clone https://github.com/DimaYankovskiy/kitchen-service.git
cd kitchen_service
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Features

* Authentication functionality for Cook (AbstractUser);
* CRUD for Dish, DishType, Ingredient models.

## Other

* New users can be created only through the admin panel;
* The middle table for the DishIngredient model is not fully used (ingredient_mass field), I will implement the logic for it in the future.

## Demo

![Website interface](demo.png)
