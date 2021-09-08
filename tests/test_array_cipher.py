from sources.array_cipher import *

def test_output_dimensions():
    input_array = np.random.rand(10,10,3)    
    array_under_test = array_cipher(input_array, "T")
    
    returned_array = array_under_test.get_ciphered_array()

    assert input_array.shape == returned_array.shape

def test_plaintext_parsing():
    input_array = np.random.rand(10,10,3)     
    array_under_test = array_cipher(input_array, "TEST")

    actual = array_under_test.plaintext_to_array()
    expected = np.array([84,69,83,84])

    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])