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

while n_choice > 0:
    print("Dica: " +  words[choice_c])
    answer_user = input("Data: DDMMAAA\n")