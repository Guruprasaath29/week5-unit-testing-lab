from example1 import is_even

def test_is_even():
    assert is_even(2) == True
    assert is_even(10) == True
    assert is_even(3) == False
    assert is_even(17) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-7) == False
