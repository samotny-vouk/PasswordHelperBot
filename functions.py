from random import choice, choices, shuffle
from itertools import permutations, product


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_CH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z']
UPPERCASE_CH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

ANSWERS = ['Увеличьте длину вашего пароля. Минимальная длина надежного пароля - 8 символов.',
           'Добавьте в ваш пароль строчные буквы.',
           'Добавьте в ваш пароль прописные буквы.',
           'Добавьте в ваш пароль цифры.',
           'Добавьте в ваш пароль символы.']

def password():
    parts = (choices(DIGITS, k=3) + choices(LOWERCASE_CH, k=3) +
             choices(UPPERCASE_CH, k=3) + choices(SYMBOLS, k=3))
    shuffle(parts)

    return "".join([str(i) for i in parts])


def check_password(pswrd):
    f = open('check_password.txt', mode="w+", encoding='utf-16')

    isStrong = True
    low = pswrd[0].islower()
    up = pswrd[0].isupper()
    dgt = pswrd[0].isdigit()
    smbl = pswrd[0] in SYMBOLS

    for i in pswrd:
        low = low or i.islower()
        up = up or i.isupper()
        dgt = dgt or i.isdigit()
        smbl = smbl or (i in SYMBOLS)

    if len(pswrd) < 8:
        f.write(ANSWERS[0] + '\n')
        print(23)
        isStrong = False
    if not low:
        f.write(ANSWERS[1] + '\n')
        isStrong = False
    if not up:
        f.write(ANSWERS[2] + '\n')
        isStrong = False
    if not dgt:
        f.write(ANSWERS[3] + '\n')
        isStrong = False
    if not smbl:
        f.write(ANSWERS[4] + '\n')
        isStrong = False

    if isStrong:
        f.write('У вас надежный пароль')
    else:
        f.write('\nВаш пароль ненадежен, чтобы улучшить его, следуйте рекомендациям, приведенным выше.')

    f.seek(0)
    result = f.read()

    f.close()
    print(result)
    return result
