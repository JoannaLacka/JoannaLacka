import random

x = random.randrange(1,10)
y = random.randrange(1,10)
score = x + y
exercise = f"{x} + {y} = "
user_score = input(exercise)

if(user_score == str(score)):
    print("Good job!")
else:
    print("Wrong answer")
