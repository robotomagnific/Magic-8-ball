# we made x choose a random integer which is tied to a dictionary item in random_key_value_pair
#make sure dictionary is turned into list or it will give index errors 
from dictionary_test import my_dictionary
import random
y = len(my_dictionary)
x = random.randint(0,y)

random_key_value_pair = list(my_dictionary.items())[x]

#by assigning variables to the index positions in random_key_value_pair you can separate the key and value while still having a random item from the dictionary list
key = random_key_value_pair[0]
value = random_key_value_pair[1]

print (key)

print (value)
