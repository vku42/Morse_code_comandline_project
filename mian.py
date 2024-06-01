from mors import MORSE_CODE_DICT
# function to encript the word
def encript(word):
    morse_code = ""
    for letter in word:
        if letter != " ":
            morse_code += MORSE_CODE_DICT.get(letter) + " "
        elif letter == " ":
            morse_code += " "
    return morse_code

# function to decript a word
def decript(enc_word):
    word_list = enc_word.split(" ")
    de_list = []
    for letter in word_list:
        if letter != '':
            de_list += [key.title() for key, value in MORSE_CODE_DICT.items() if value == letter]
        elif letter == '':
            de_list += " "
    if de_list == []:
        return "please somtning valid"
    return "".join(de_list)

# main morsecode function
def moresecode_fun(word, fun):
    if fun == "en":
        return encript(word)
    elif fun == "de":
        return decript(word)

# function logic
while True:
    to_perform = input("Please tell which function to perform en: 'for encript and de: 'for decript' and 'none' to exit: ").lower()
    if to_perform == "none":
        break
    elif to_perform == "en" or to_perform == "de":
        user_input = input("Please enter the word you want to convert: ").upper()
        print(moresecode_fun(user_input, to_perform))
    else:
        print("Pease Enter something valid")
