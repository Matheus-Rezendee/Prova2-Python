def is_palindrome(word):
    return word == word[::-1]

user_input = input("Digite uma palavra: ")

if is_palindrome(user_input):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
