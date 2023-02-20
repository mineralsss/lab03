'''Q1  (2.5 marks). Dice Throws 


You are required to develop a program that will throw two dice until the top faces of the two dice total to a specified number (use random function to generate Dice). '''
import random
print ("Dice thrower!")
print ("______________")
while True:
    try:
        total = int(input("Input your desire number: "))
        if total < 1 or total > 12:
            print("Invalid number")
        else:
            break
    except ValueError:
        print("Please eneter a number")
count = 0
first_dice = 0
second_dice = 0
while total != first_dice + second_dice:
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    count += 1
    print("Result of throw ", count, ":", first_dice + second_dice)
print("You get your desired number in ", count, "throw")

