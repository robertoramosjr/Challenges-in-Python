"""
*Criar variáveis para nome (str), idade (int),
*altura (float) e peso (float) de uima pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-strings (com as chaves)

"""

nome = 'Roberto'
idade = 29
altura = 1.81
e_maior = idade > 18
peso = 110
imc = peso / altura ** 2
ano_atual = 2022
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'o IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')