"""
create an algorithm that checks if a CPF is valid or not.
"""


def turn_in_list_of_int():
    global cpf_in_list, cpf_in_int_list
    for n in cpf_in_list:
        int_n = int(n)
        cpf_in_int_list.append(int_n)


def eleventh_digit_validation_calculus():
    global sum_eleventh_digit
    return 11 - (sum_eleventh_digit % 11)


def tenth_digit_validation_calculus():
    global sum_tenth_digit
    return 11 - (sum_tenth_digit % 11)


def define_digit_ten():
    return 0 if tenth_digit_validation > 9 else tenth_digit_validation


def define_digit_eleven():
    return 0 if eleventh_digit_validation > 9 else eleventh_digit_validation


def calculate_ten_digit():
    global sum_tenth_digit, x
    while x <= 8:
        multiplied_number = cpf_in_int_list[x] * factors_to_check_tenth_digit[x]
        sum_tenth_digit += multiplied_number
        x += 1
    return sum_tenth_digit


def calculate_eleven_digit():
    global sum_eleventh_digit, y
    while y <= 9:
        new_multiplied_number = cpf_in_int_list[y] * factor_to_check_eleventh_digit[y]
        sum_eleventh_digit += new_multiplied_number
        y += 1
    return sum_eleventh_digit


sum_tenth_digit = 0
x = 0
sum_eleventh_digit = 0
y = 0
factor_to_check_eleventh_digit = list(range(11, 1, -1))
factors_to_check_tenth_digit = list(range(10, 1, -1))


cpf = input('Insira seu CPF, sem pontos \n')

while not cpf.isdigit() or len(cpf) != 11:
    print('Este CPF é inválido, os possíveis CPFs admitem 11 números.')
    cpf = input('Insira seu CPF, sem pontos \n')

cpf_in_list = list(cpf)
cpf_in_int_list = []

for number in cpf_in_list:
    number_as_int = int(number)
    cpf_in_int_list.append(number_as_int)

sum_tenth_digit = calculate_ten_digit()

tenth_digit_validation = tenth_digit_validation_calculus()

digit_ten = define_digit_ten()

sum_eleventh_digit = calculate_eleven_digit()

eleventh_digit_validation = eleventh_digit_validation_calculus()

digit_eleven = define_digit_eleven()

sequence = cpf[0] * len(cpf)

print('CPF válido') if digit_ten == cpf_in_int_list[-2]\
    and digit_eleven == cpf_in_int_list[-1]\
    and cpf != sequence \
    else print('CPF inválido')