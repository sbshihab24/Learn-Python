name='Mehedi Hasan Shihab'
print(name)



# Creating Strings

s1="Hello"
s2='World'
s3=""" This is multi line string"""

print(s1)
print(s2)
print(s3)

#String Methods

text=" Hello World"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("World","Python"))


#String Checking

msg ="Python is fun"
print("Python" in msg)
print("Java" in msg)

#String Formatting

name=input("What is your name?")
age=input("How old are you?")

print(f"Hello {name},you are {age} years old")
print("My name is {} and I am {} years old.".format(name, age))


name = input("Enter your name: ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())

#Reverse a string.

text= "Python"
print("Reversed: ",text[::-1])

#Check if a word is a palindrome

word=input("Enter a word: ")
if word==word[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")


