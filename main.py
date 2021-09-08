from PIL import Image
import array_cipher
import numpy as np

from sources import array_cipher

# "Nature bird" by @Doug88888 is licensed with CC BY-NC-SA 2.0. 
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/2.0/ 

an_image = Image.open("nature_bird.jpg")
image_array = np.array(an_image)

image_cipherator = array_cipher.array_cipher(image_array, "This message is encrypted")
output_array = image_cipherator.get_ciphered_array()

PIL_image = Image.fromarray(output_array, 'RGB')
PIL_image.save('output.bmp')