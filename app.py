'''Simple flask app to serve random recipes.'''

from flask import Flask
from ProductionCode.data import get_data
from ProductionCode.random_recipe import get_random_recipes

app = Flask(__name__)

@app.route('/')
def homepage():
    '''Return a simple message for the homepage.'''
    return "To use this app go to /random/&lt;int:num_recipes&gt; where &lt;int:num_recipes&gt; " \
    "is the number of random recipes you want to get. For example, /random/5 will return " \
    "5 random recipes."


@app.route('/random/<int:num_recipes>', strict_slashes=False)
def random_recipes(num_recipes):
    '''Return some number of random recipes.'''

    data = get_data('recipe_data.csv', 'Data')
    recipes = get_random_recipes(data, num_recipes)
    formatted_recipes = format_all_recipes(recipes)

    return formatted_recipes

def format_all_recipes(recipes):
    '''Format all recipes for display.'''

    formatted_recipes = []
    for recipe in recipes:
        formatted_recipes.append(format_recipe(recipe))

    return "<br><br>".join(formatted_recipes)

def format_recipe(recipes):
    '''Format the recipe data for display.'''

    recipe_string = f"Recipe: {recipes[1]}<br>"
    recipe_string += f"Instructions: {recipes[2]}<br>"
    recipe_string += f"Ingredients: {recipes[3]}<br>"
    recipe_string += "-------------------------<br>"

    return recipe_string

@app.errorhandler(404)
def page_not_found(e):
    '''Return a custom 404 error message.'''
    return "sorry, wrong format, / or /random/<int:num_recipes> expected" + str(e), 404


@app.errorhandler(500)
def python_bug(e):
    '''Return a custom 500 error message.'''
    print(e)
    return "Python Bug. You likely are requesting more random recipes than exist." + str(e), 500


if __name__ == '__main__':
    app.run()
