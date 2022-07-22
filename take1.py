from math import pow, sqrt# built-in python module that gives users access to various athematical operations and functions
import random as random# built-in python


result_1 = pow(2,4) 
print("result_1 is", result_1)

result_2= sqrt(16)
print("result_2 is", result_2)


result_3=random.randint(0,100)
print("result_3 is", result_3)

names= ["Amaryllis","Godson","Emily","Reina","Derin","Elena","Inacio"]
print("Original names: ",names)

random.shuffle(names)
print("Names after shuffling: ",names)

result_4=random.choice(names)
print("Chosen name is: ",result_4)