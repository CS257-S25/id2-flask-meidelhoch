'''
Test the Flask application for getting a random recipe.
'''

import unittest
import unittest.mock
import random
from app import *



class TestHome(unittest.TestCase):
    '''Test the homepage route.'''
    def test_route(self):
        '''Test the homepage route.'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"To use this app go to /random/&lt;int:num_recipes&gt; where "
        b"&lt;int:num_recipes&gt; is the number of random recipes you want to get. For example, "
        b"/random/5 will return 5 random recipes.", response.data)

class TestRandomRecipes(unittest.TestCase):
    '''Test the random recipes route.'''
    def setUp(self):
        '''
        Sets up the test environment by mocking the get_data function.
        '''

        random.seed(73191)

        self.patcher = unittest.mock.patch('app.get_data')
        self.mock_get_data = self.patcher.start()
        self.mock_get_data.return_value = [
            ['0', 'Title1', 'Instructions for Title1', ['Ingredient1', 'Ingredient2']],
            ['1', 'Title2', 'Instructions for Title2', ['Ingredient3', 'Ingredient4']],
            ['2', 'Title3', 'Instructions for Title3', ['Ingredient5', 'Ingredient6']],
            ['3', 'Title4', 'Instructions for Title4', ['Ingredient7', 'Ingredient8']],
            ['4', 'Title5', 'Instructions for Title5', ['Ingredient9', 'Ingredienta']],
            ['5', 'Title6', 'Instructions for Title6', ['Ingredientb', 'Ingredientc']],
            ['6', 'Title7', 'Instructions for Title7', ['Ingredientd', 'Ingrediente']],
            ['7', 'Title8', 'Instructions for Title8',
             ['Ingredientf', 'Ingredientg', 'Ingredient3']],
            ['8', 'Title9', 'Instructions for Title9',
             ['Ingredienth', 'Ingredienti', 'Ingredient7', 'Ingredient1']],
            ['9', 'Title10', 'Instructions for Title10',
             ['Ingredient4', 'Ingredient8', 'Ingrediente']]
        ]

    def tearDown(self):
        '''
        Stops the patcher after the test.
        '''
        self.patcher.stop()

    def test_valid_input(self):
        '''Test the random recipes route.'''
        self.app = app.test_client()
        response = self.app.get('/random/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe: Title7", response.data)
        self.assertIn(b"Instructions: Instructions for Title7", response.data)
        self.assertIn(b"Ingredients: ['Ingredientd', 'Ingrediente']", response.data)

        response = self.app.get('/random/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe: Title5", response.data)
        self.assertIn(b"Instructions: Instructions for Title5", response.data)
        self.assertIn(b"Ingredients: ['Ingredient9', 'Ingredienta']", response.data)
        self.assertIn(b"Recipe: Title10", response.data)
        self.assertIn(b"Instructions: Instructions for Title10", response.data)
        self.assertIn(b"Ingredients: ['Ingredient4', 'Ingredient8', 'Ingrediente']", response.data)

    def test_invalid_input(self):
        '''Test the random recipes route with invalid input.'''
        self.app = app.test_client()
        response = self.app.get('/random/abc', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"sorry, wrong format, / or /random/<int:num_recipes> expected",
                      response.data)

        response = self.app.get('/random/-1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"sorry, wrong format, / or /random/<int:num_recipes> expected",
                      response.data)

        response = self.app.get('/random/1000', follow_redirects=True)
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Python Bug. You likely are requesting more random recipes than exist.",
                      response.data)
