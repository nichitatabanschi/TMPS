from abc import ABC, abstractmethod


# Complex object Meal
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        return ", ".join(self.items)


# Abstract Builder
class MealBuilder(ABC):
    @abstractmethod
    def add_main_course(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass

    @abstractmethod
    def add_dessert(self):
        pass


# Concrete Builder for a Combo Meal
class ComboMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self):
        self.meal.add_item("Burger")

    def add_drink(self):
        self.meal.add_item("Soda")

    def add_dessert(self):
        self.meal.add_item("Ice Cream")

    def get_meal(self):
        return self.meal


# Director class that builds a meal
class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_meal(self):
        self.builder.add_main_course()
        self.builder.add_drink()
        self.builder.add_dessert()
        return self.builder.get_meal()
