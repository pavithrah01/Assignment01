word = input("Enter the word to reverse")
reversed_word = ''
for letter in word:
    reversed_word = letter + reversed_word
print(reversed_word)