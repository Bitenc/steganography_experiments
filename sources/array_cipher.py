import numpy as np
from sources import number_operations


class array_cipher:

    array = np.empty(0)
    plaintext = ""

    def __init__(self, input_array, input_text):
        self.array = input_array
        self.plaintext = input_text

    def plaintext_to_array(self):
        return_array = []
        for i in range(0,len(self.plaintext)):
            return_array.append(ord(self.plaintext[i]))
        return np.asarray(return_array, dtype="uint8")

    def get_ciphered_array(self):
        array_shape = self.array.shape
        self.array = self.array.ravel()

        plaintext_bits = np.unpackbits(self.plaintext_to_array())

        for i in range(0, len(plaintext_bits)):
            if(plaintext_bits[i] == 1):
                self.array[i] = number_operations.make_even(self.array[i])
            elif(plaintext_bits[i] == 0):
                self.array[i] = number_operations.make_odd(self.array[i])

        self.array = self.array.reshape(array_shape)
        return self.array