import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for index, row in df.iterrows()}


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_input = input('Enter a word:').upper()
    list_of_letters = [letter for letter in user_input]
    try:
        nato_translation_list = [nato_dict[letter] for letter in list_of_letters]
    except KeyError:
        print('Sorry, only letters in the alphabet please!')
        generate_phonetic()
    else:
        print(nato_translation_list)


generate_phonetic()