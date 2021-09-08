from sources.number_operations import *

def test_make_even():
    assert 254 == make_even(255)
    assert 254 == make_even(256)
    assert 0 == make_even(0)
    assert 2 == make_even(1)

def test_make_odd():
    assert 255 == make_odd(255)
    assert 255 == make_odd(256)
    assert 1 == make_odd(0)
    assert 1 == make_odd(1)
    
    