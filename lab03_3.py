#1.	Removal all characters from a string except integers
str = input("Enter a string: ")
new_str1 = ""
for i in str:
    if i.isdigit():
        new_str1 += i
if new_str1 == "":
    print("There is no digit in the string")
else:
    print("Output 1: ",new_str1)
#2.	Remove special symbols / punctuation from a string
new_str2 = ""
for i in str:
    if i.isalpha() or i.isdigit() or i == " ":
        new_str2 += i
print("Output 2: ",new_str2)

