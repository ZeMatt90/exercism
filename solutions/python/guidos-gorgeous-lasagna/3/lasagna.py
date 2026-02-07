"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME: int = 40
PREPARATION_TIME: int = 40

def bake_time_remaining(elapsed_bake_time: int)-> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(numer_of_layers: int)->int:
    """
    doc
    """
    return numer_of_layers*2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    doc
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
#1
print(EXPECTED_BAKE_TIME)
#2
bake_time_remaining(30)
#3
preparation_time_in_minutes(2)
#4
elapsed_time_in_minutes(3, 20)