# Assignment 3 Quenstion No. 1
word = input("Please enter a word: ").lower()
vowel_count = 0

for char in word:
    if char in "aeiou":
        vowel_count += 1

print(f"The number of vowels in the word '{word}' is {vowel_count}.")


# Assignment 3 Question 2
word = input("Please enter a word: ")
print(word)

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for char in word:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1

print(f"The input word contains {upper_count} uppercase letters, {lower_count} lowercase letters, {digit_count} digits, and {space_count} spaces.")


# Assignment 3 Question 3
word = input("Enter a word: ")
char_list = list(word)
first_char = char_list.pop(0)
last_char = char_list.pop(-1)
char_list.append(first_char)
char_list.insert(0, last_char)
new_word = "".join(char_list)
print(new_word)


# Assignment 3 Question 4
word = input("Write a word: ")

for i in range(-1, -len(word)-1, -1):
    print(word[i], end="")


# Assignment 3 Question 5    
word = input("Please enter a word: ")
char_list = list(word)
first_char = char_list.pop(0)
char_list.append(first_char)
new_word = "".join(char_list)
print(new_word)

# Assignment 3 Question 6
word = input("Please enter a word: ")
word_list = word.split()

for item in word_list:
    print(item[0])

# Assignment 3 Question 7
word = input("Please enter a word: ")
char_list = list(word)
reversed_list = []

for i in range(-1, -len(word)-1, -1):
    letter = char_list.pop(-1)
    reversed_list.append(letter)

reversed_word = "".join(reversed_list)

if word == reversed_word:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")

# Assignment 3 Question 7
word = input("Enter a word: ")
reversed_word = word[::-1]

if word == reversed_word:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")


# Assignment 3 Question 8
word = input("Enter a word: ")

for i in range(len(word)):
    word = word[1:] + word[0]
    print(word)

# Assignmexnt 3 Question 9
def password_checker():
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password should be at least 8 characters.")
        return

    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)

    if not upper:
        print("Your password should contain at least one uppercase letter.")
    elif not lower:
        print("Your password should contain at least one lowercase letter.")
    elif not digit:
        print("Your password should contain at least one digit.")
    else:
        print("Password Accepted!")
