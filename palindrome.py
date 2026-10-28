# Python program to check whether the word is palindrome or not

text=input("Enter the text/word : ")

if text == text[::-1]:
 print(f"{text} is a palindrome")
else:
 print(f"{text} is not a palindrome")