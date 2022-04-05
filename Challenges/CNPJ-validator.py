"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import re


def ask_cnpj():
    return input('Qual o CNPJ? \n')


def format_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def cloning_cnpj(cnpj):
    return cnpj[:-2]


def lists_to_check():
    return [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def check_first_digit():
    temp_value = sum([int(checker[n]) * to_check_first[n] for n in range(len(checker))])
    checker.append(str(calculate_digit(temp_value)))


def check_second_digit():
    temp_value = sum([int(checker[n]) * to_check_second[n] for n in range(len(checker))])
    checker.append(str(calculate_digit(temp_value)))


def calculate_digit(value):
    return 11 - (value % 11) if 11 - (value % 11) < 9 else 0


def compare_cnpjs():
    print('O cnpj é válido') if checker == cnpj else print('O cnpj é inválido')


cnpj = ask_cnpj()

cnpj = list(format_cnpj(cnpj))

checker = cloning_cnpj(cnpj)

to_check_first, to_check_second = lists_to_check()

check_first_digit()

check_second_digit()

compare_cnpjs()

