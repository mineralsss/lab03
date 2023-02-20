#Write a program that permits user entering some characters until the ENTER key  is pressed. The program will print out the number of digits, number of letters, number of other keys were pressed
str = input("Enter some characters: ")
digit = 0   
letter = 0
other = 0
for i in str:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letter += 1
    else:
        other += 1
print("Number of digits: ", digit)
print("Number of letters: ", letter)
print("Number of other keys: ", other)