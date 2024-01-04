from faker import Faker
import random

a=  Faker()
for i in range(100):
    with open('text.txt','a') as file:
        str_ = str(f"{i+1} {a.name()} {random.randint(10,90)}")
        file.write(f"{str_}\n")
