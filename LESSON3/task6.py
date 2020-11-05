def word_capitalize(word:str)->str:
    return word.capitalize()


def string_capitalize()->str:
    l=[]
    user_string=input('Enter the line of words separated by spaces:\n')
    for words in user_string.split(' '):
        l.append(word_capitalize(words))
    return (' '.join(l))


print(string_capitalize())