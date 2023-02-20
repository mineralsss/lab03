#Write a program (using functions) that requires the user to provide a long string containing many words. Print back to the user a new string with the word order reversed from the original list. For example, when the user enters the string:
str = input("Enter a string: ")
new_str = str.split()
reversed_str = new_str[::-1]
reversed_sentence = " ".join(reversed_str)
print(reversed_sentence)
