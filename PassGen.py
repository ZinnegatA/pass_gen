from random import sample

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''
flag = True

print('Вас приветствует программа генерации безопасных паролей! Для начала ответьте на несколько уточняющих вопросов.')
print()
pass_amount = input('Введите количество паролей, которые Вы хотите сгенерировать: ')
pass_len = input('Какой длины должен быть пароль? Введите количество желаемых символов: ')
pass_num = input('Включать ли в пароль цифры? ')
pass_alpha = input('Включать ли в пароль прописные буквы? ')
pass_lower = input('Включать ли в пароль строчные буквы? ')
pass_symbols = input('Включать ли в пароль символы? ')
pass_unus_symb = input('Хотите исключить из пароля неоднозначные символы (i, l, 1, L, o, 0, O)? ')

if pass_num in ['да', 'д']:
    chars += DIGITS
if pass_alpha in ['да', 'д']:
    chars += UPPERCASE_LETTERS
if pass_lower in ['да', 'д']:
    chars += LOWERCASE_LETTERS
if pass_symbols in ['да', 'д']:
    chars += PUNCTUATION
if pass_unus_symb in ['да', 'д']:
    for c in 'il1Lo0O':
        chars.replace(c, '')


def generate_password(length, symbols):
    return sample(symbols, length)


while flag:
    for i in range(1, int(pass_amount) + 1):
        print(''.join(generate_password(int(pass_len), chars)))
    newtry = input('Хотите сгенерировать новые пароли? ')
    if newtry.lower() in ['да', 'д']:
        flag = True
    else:
        print('Спасибо, что пользовались моим генератором паролей!')
        flag = False
