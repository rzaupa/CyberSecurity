import random
import string

characters=string.ascii_letters
password=''
for i in range(10):
    password=password+random.choice(characters)

print("La password generata è ",password)