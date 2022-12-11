import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


if nr_letters > 0:
    x = random.choices(letters, k=nr_letters)
    letras = "".join(x)
    if nr_symbols > 0:
        x1 = random.choices(symbols, k=nr_symbols)
        letras += "".join(x1)
        if nr_numbers > 0:
            x2 = random.choices(numbers, k=nr_numbers)
            letras += "".join(x2)
random.shuffle(letras)
print(letras)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for letra in letters:
#     if nr_letters > 0:
#         adiciona1 = random.choices(letra, k=nr_letters)
#         letras = "".join(adiciona1)
# for numero in numbers:
#     adiciona2 = random.choices(numero, k=nr_numbers)
#     letras += "".join(adiciona2)
# for simbolo in symbols:
#     adiciona3 = random.choices(simbolo, k=nr_symbols)
#     letras += "".join(adiciona2)
# print(letras)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
