# 13
import random
number = random.randrange(1, 20)
cnt = 1
name = str(input("Hello! What is your name?\n"))
print('Well', name,  "I am thinking of a number between 1 and 20. Take a guess.", sep = ", ")
UserNum = int(input())

while UserNum != number:
    if UserNum > number:
        print("Your guess is too high.")
        cnt += 1
    elif UserNum < number:
        print("Your guess is too low.")
        cnt += 1
    UserNum = int(input("Take a guess.\n"))
print("Good job,", name, "You guessed my number in", cnt, "guesses!")
