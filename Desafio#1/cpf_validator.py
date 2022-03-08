"""
create an algorithm that checks if a CPF is valid or not.
"""
sum_tenth_digit = 0
x = 0
sum_eleventh_digit = 0
y = 0

cpf = input('Insira seu CPF, sem pontos \n')

while len(cpf) != 11:
    print('O CPF possui apenas 11 dígitos, digite um CPF válido.')
    cpf = input('Insira seu CPF, sem pontos \n')

cpf_in_list = list(cpf)
cpf_in_int_list = []

for number in cpf_in_list:
    number_as_int = int(number)
    cpf_in_int_list.append(number_as_int)

factors_to_check_tenth_digit = list(range(10, 1, -1))

while x <= 8:
    multiplied_number = cpf_in_int_list[x] * factors_to_check_tenth_digit[x]
    sum_tenth_digit += multiplied_number
    x += 1

tenth_digit_validation = 11 - (sum_tenth_digit % 11)

if tenth_digit_validation > 9:
    digit_ten = 0
else:
    digit_ten = tenth_digit_validation

factor_to_check_eleventh_digit = list(range(11, 1, -1))

while y <= 9:
    new_multiplied_number = cpf_in_int_list[y] * factor_to_check_eleventh_digit[y]
    sum_eleventh_digit += new_multiplied_number
    y += 1

eleventh_digit_validation = 11 - (sum_eleventh_digit % 11)

if eleventh_digit_validation > 9:
    digit_eleven = 0
else:
    digit_eleven = eleventh_digit_validation

if digit_ten == cpf_in_int_list[-2] and digit_eleven == cpf_in_int_list[-1]:
    print('CPF válido')
else:
    print('CPF inválido')