import pandas

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO = {}

for (index, row) in data.iterrows():
    NATO[row.letter] = row.code

print(NATO)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Please enter a word: ")
phonetic_words = [NATO[letter] for letter in word.upper()]
print(phonetic_words)
