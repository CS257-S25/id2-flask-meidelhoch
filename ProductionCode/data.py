'''
This module contains functions to read in our data from a CSV file and clean it so it is usable.
'''

import os
import csv
import ast

def get_data(filename, folder):
    """
    Returns the cleaned data from the given csv.
    """

    file_path = get_filepath(filename, folder)

    data = read_file(file_path)

    cleaned_data = clean_data(data)

    return cleaned_data

def get_filepath(filename, folder):
    """
    Returns the file path of the given filename in the given folder.
    """
    data_folder = os.path.join(os.path.dirname(__file__), f'../{folder}')
    file_path = os.path.join(data_folder, filename)

    return file_path

def clean_data(data):
    """
    Cleans the data by removing the header and cleaning each line.
    """

    cleaned_data = [clean_line(line) for line in data[1:]]

    return cleaned_data

def read_file(file_path):
    """
    Reads a file and returns its contents.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = list(csv.reader(f))

    return data

def clean_line(line):
    """
    Cleans a line of data by converting the ingredients into a python list.
    """

    line[3] = fix_ingredients(line[3])

    return line

def fix_ingredients(ingredients_string):
    """
    Takes a string of ingredients and converts it into a python list.
    """
    ingredients_array = ast.literal_eval(ingredients_string)

    return ingredients_array
