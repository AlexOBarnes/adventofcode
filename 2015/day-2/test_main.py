'''Tests for solution main.py'''
import pytest
from main import find_sides, calculate_area,get_wrapping,get_perimeter,get_bow

class TestFindSides:

    def test_valid_input(self):
        assert find_sides('2x3x4\n') == [2,3,4]

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            assert find_sides(2)

class TestCalculateArea:

    def test_valid_input(self):
        assert calculate_area([2,3,4]) == [12,16,24]

class TestGetWrapping:

    def test_valid_input(self):
        assert get_wrapping([2,3,4]) == 10


class TestGetPerimeter:

    def test_valid_input(self):
        assert get_perimeter([2,3,4]) == 10

class TestGetBow:
    
    def test_valid_input(self):
        assert get_bow([2,3,4]) == 24