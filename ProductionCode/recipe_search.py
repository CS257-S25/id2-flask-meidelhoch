'''This file deals with the recipe search function'''

def find_recipes(recipe_data, wanted_ingredients, unwanted_ingredients):
    '''Find recipes that match the wanted and unwanted ingredients.'''
    matching_recipes = []
    for recipe in recipe_data:
        recipe_ingredients = get_ingredients(recipe)
        if valid_recipe(recipe_ingredients, wanted_ingredients, unwanted_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def get_ingredients(recipe):
    '''Get the ingredients from a recipe.'''
    return recipe[3]

def valid_recipe(recipe_ingredients, wanted_ingredients, unwanted_ingredients):
    '''Check if a recipe is valid based on the wanted and unwanted ingredients.'''
    for wanted_ingredient in wanted_ingredients:
        if not contains_wanted_ingredient(wanted_ingredient, recipe_ingredients):
            return False
    for unwanted_ingredient in unwanted_ingredients:
        if contains_unwanted_ingredient(unwanted_ingredient, recipe_ingredients):
            return False
    return True


def contains_wanted_ingredient(wanted_ingredient, recipe_ingredients):
    '''Check if a wanted ingredient is in the recipe.'''
    for ingredient in recipe_ingredients:
        if wanted_ingredient in ingredient:
            return True
    return False

def contains_unwanted_ingredient(unwanted_ingredient, recipe_ingredients):
    '''Check if an unwanted ingredient is in the recipe.'''
    for ingredient in recipe_ingredients:
        if unwanted_ingredient in ingredient:
            return True
    return False
