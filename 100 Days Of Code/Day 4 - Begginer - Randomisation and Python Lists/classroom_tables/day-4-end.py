import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.000000... - 0.999999...
random_float = random.random()
print(random_float)

#0.000... - 4.999...
random_float = random_float * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love socre is {love_score}")
