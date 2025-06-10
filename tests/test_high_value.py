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

def test_add_to_first_value():
    first_value = HighValue(3,5)
    first_value.add(10,"first")
    assert first_value.value_first == 13

def test_add_to_second_value():
    second_value = HighValue(3,5)
    second_value.add(10,"second")
    assert second_value.value_second == 15

def test_first_second_return_equal():
    equal_values = HighValue(5,5)
    result = equal_values.get_highest()
    assert result == "Values are equal"

def test_first_value_negative_and_highest():
    first_value = HighValue(-5,-8)
    result = first_value.get_highest()
    assert result == "First value is higher"

def test_second_value_negative_and_highest():
    second_value = HighValue(-10,-8)
    result = second_value.get_highest()
    assert result == "Second value is higher"

def test_values_equal_to_zero():
    zero_value = HighValue(0,0)
    result = zero_value.get_highest()
    assert result == "Values are equal"

def test_adding_to_first_value_checking_highest():
    adding_values = HighValue(3,5)
    adding_values.add(10, "first")
    result = adding_values.get_highest()
    assert result == "First value is higher"

def test_adding_to_second_value_checking_highest():
    adding_values = HighValue(3,5)
    adding_values.add(10, "second")
    result = adding_values.get_highest()
    assert result == "Second value is higher"