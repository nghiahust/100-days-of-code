import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter:row.code for (index, row) in df.iterrows()}
input_name = input("Type a words")
for char in input_name:
