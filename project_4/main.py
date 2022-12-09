import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

escolha = input("Escolha entre 'pedra' 'papel' 'tesoura'\n:")

lista = ["pedra", "papel", "tesoura"]

x = random.randint(0, len(lista))

final = lista[x -1]

if escolha == "papel" and final  == "pedra":
    print(f"Voce ganhou\n{papel}")
elif escolha == "pedra" and final == "tesoura":
    print(f"Voce ganhou\n{pedra}")
elif escolha == "tesoura" and final == "papel":
    print(f"Voce ganhou\n{tesoura}")
elif final == "papel" and escolha  == "pedra":
    print(f"Voce perdeu\n{papel}")
elif final == "pedra" and escolha == "tesoura":
    print(f"Voce perdeu\n{pedra}")
elif final == "tesoura" and escolha == "papel":
    print(f"Voce perdeu\n{tesoura}")
else:
    print(f"Empate Sua escolha'{escolha}' vs Computador '{final}'")