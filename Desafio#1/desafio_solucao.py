"""
*Criar variáveis para nome (str), idade (int),
*altura (float) e peso (float) de uima pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-strings (com as chaves)

"""

name = input('Qual seu nome?')
age = int(input ('Qual sua idade?'))
height = float(input('Qual sua altura?'))
weight = int(input('Qual seu peso? (em kg)'))
imc = weight / height ** 2
nowaday_year = input('Que ano você está?')
birth_year = nowaday_year - age

print(f'{name} tem {age} anos, {height} de altura e pesa {weight} kg.')
print(f'o IMC de {name} é {imc:.2f}.')
print(f'{name} nasceu em {birth_year}.')