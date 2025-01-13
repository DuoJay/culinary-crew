#!/usr/bin/env python
import sys
import warnings

from crew import Culinarycrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

ingredients_input = input("Please tell me your recipe ingredients:")

def run():
    """
    Run the culinary crew to create a recipe, enrich it with ingredients, provide cooking instructions,
    and recommend music based on the recipe's origin.
    """

    inputs = {
        'ingredients': ingredients_input,
    }
    
    Culinarycrew().crew().kickoff(inputs=inputs)

run()