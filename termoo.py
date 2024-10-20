""" Utilizzando json
    "open" serve para abrir arquivos dentro do script
"""
import json
import random

f = open("words.json", encoding="utf8")

words = json.load(f)
print(words.keys())
choice_c = random.choice(list(words.keys()))

print("Olá, seja bem vindo!")
print("###############################")

n_choice = 5
win = False

while n_choice > 0 and win is not True:
    print("Dica: " +  words[choice_c])
    answer_user = input("Data: DDMMAAA\n")

    if len(answer_user) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos!")
        continue
    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("C")
                pontuation = pontuation + 1
            else:
                check.append("E")

        print("Resporta: \n")
        print(" |".join(check))
        print(" |".join(answer_user))
        print("##################### \n")
        if pontuation == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data! ")
        continue
    n_choice = n_choice - 1

if win == True:
    print("Vitória!!")
else:
    print("Derrota!")
    print("A resposta correta era: " + choice_c)