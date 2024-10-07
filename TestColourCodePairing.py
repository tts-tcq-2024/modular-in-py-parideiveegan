import unittest
from GetColourFromPairNumber import get_color_from_pair_number
from GetPairNumberFromColour import get_pair_number_from_color

class TestCoulurCodePairing(unittest.TestCase):

  def test_number_to_pair(self):
    major_color, minor_color = get_color_from_pair_number(1)
    assert(major_color == "White")
    assert(minor_color == "Blue")

  def test_pair_to_number(self):
    pair_number = get_pair_number_from_color("White", "Blue")
    assert(pair_number == 1)

if __name__ == '__main__':
    unittest.main()
