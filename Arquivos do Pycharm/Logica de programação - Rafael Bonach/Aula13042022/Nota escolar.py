def entra_nota(mensagem):
    nota = float(input(mensagem + '? '))
    if nota < 0 or nota > 10:
        print('A nota está com valor inválido!')
        exit()
    return nota

n1 = entra_nota('Qual a primeira nota')
n2 = entra_nota('Qual a segunda nota')
n3 = entra_nota('Qual a terceira nota')
media = (n1 + n2 + n3)/3
if media >= 7:
        print('Você passou com nota {}'.format(media))
else:
    print('Você reprovou com nota {}'.format(media))