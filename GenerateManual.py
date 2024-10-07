from GetColourFromPairNumber import get_color_from_pair_number
from GetPairNumberFromColour import get_pair_number_from_color

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def generate_manual():
    """Generates a manual of color pairs."""    
    for pair_number in range(1, 26):
        major, minor = get_color_from_pair_number(pair_number)
        print(f'{pair_number}: {color_pair_to_string(major, minor)}')
