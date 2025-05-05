'''
This module contains a function to get a random recipe from a list of recipes.
'''
import random

def get_random_recipes(recipes, num_recipes):
    """
    Returns a random recipe from the given list of recipes.
    """

    return random.sample(recipes, num_recipes)
