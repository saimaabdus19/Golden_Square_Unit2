from lib.high_value import * 

def test_return_output_first_value():
    high_value = HighValue(3,5)
    assert high_value.value_first == 3

def test_return_output_second_value():
    high_value = HighValue(3,5)
    assert high_value.value_second == 5

def test_highest_when_first_value_highest():
    first_value = HighValue(5,3)
    result = first_value.get_highest()
    assert result == "First value is higher"

def test_highest_when_second_value_highest():
    second_value = HighValue(3, 5)
    result = second_value.get_highest()
    assert result == "Second value is higher"

def