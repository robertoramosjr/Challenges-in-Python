word = input('Insira uma palavra para ser adivinhada')

x = 6
tried_word = []
while x > 0:
    letter = input('Digite uma letra que você acha que pertence a palavra \n')

    if len(letter) > 1:
        print('Digite uma letra por vez \n')
    elif letter.isdigit():
        print('Digite apenas letras, não existem números em palavras')

    if letter in word:
        tried_word.append(letter)
        print(f'Boa!! A letra {letter} está na palavra secreta')
    else:
        print(f'Putz... A letra {letter} não está na palavra secreta')
        x -= 1

    discovered_word = ''
    for right_letter in word:
        if right_letter in tried_word:
            discovered_word += right_letter
        else:
            discovered_word += '*'

    print(f'A palavra secreta está assim {discovered_word}')

    if discovered_word == word:
        print('Parabééééns!!!!! Você ganhou!!!!!! \n',
              f'A palavra secreta é "{word.upper()}"')
        break
    elif x == 0:
        print('Infelizmente, não foi dessa vez \n',
              f'A palavra secreta era {word.upper()}')
        break
    else:
        print(f'Você tem {x} chances restantes.')
