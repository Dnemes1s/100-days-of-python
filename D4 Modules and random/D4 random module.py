import random
#Importing the random module

random_int = random.randint(1, 100)
print(random_int)
# This will print a random integer between 1 and 100

random_num_0_to_1 = random.random()
print(random_num_0_to_1)
# This will print a random float between 0.0 and 1.0
# Will include 0.0 but not 1.0

random_num_0_to_1 = random.random() * 10
print(random_num_0_to_1)
# This will print a random float between 0. and 10.0

random_float = random.uniform(1, 10)
print(random_float)
# This will print a random float between 1.0 and 10.0