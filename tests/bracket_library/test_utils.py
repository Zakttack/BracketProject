import pytest
from bracket_library.utils import greater_or_equal_power_of_two

def test_greater_or_equal_power_of_two_invalid_negative():
    with pytest.raises(ValueError, match="The number must be at least 2."):
        greater_or_equal_power_of_two(-1)
    
def test_greater_or_equal_power_of_two_invalid():
    with pytest.raises(ValueError, match="The number must be at least 2."):
        greater_or_equal_power_of_two(1)
        
def test_greater_or_equal_power_of_two_exactly_2():
    assert greater_or_equal_power_of_two(2) == 2

def test_greater_or_equal_power_of_two_non_power():
    assert greater_or_equal_power_of_two(5) == 8
    
def test_greater_or_equal_power_of_two_power():
    assert greater_or_equal_power_of_two(128) == 128