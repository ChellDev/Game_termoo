""" Utilizzando json
    "open" serve para abrir arquivos dentro do script
"""
import json
import random

f = open("words.json", encoding="utf8")

words = json.loas(f)
print(words.keys())
choice = random.choice(words.keys())
