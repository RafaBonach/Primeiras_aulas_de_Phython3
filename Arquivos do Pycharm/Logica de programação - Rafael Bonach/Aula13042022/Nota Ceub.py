def entra_nota(mensagem):
    nota = float(input(mensagem + '? '))
    if nota < 0 or nota > 10:
        print('A notá é um valor invalido!')
        exit()
    return nota

n1 = entra_nota('Qual a primeira nota')
n2 = entra_nota('Qual a segunda nota')
n3 = entra_nota('Qul a terceira nota')

mponderada = (n1*1 +n2*1.5 + n3*2)/(1+1.5+2)
if mponderada == 0:
    print('Você tirou SR')
else:
    if mponderada < 2:
        print('Você tirou II')
    else:
        if mponderada < 5:
            print('Você tirou MI')
        else:
            if mponderada < 7:
                print('Você tirou MM')
            else:
                if mponderada < 9:
                    print('Você tirou MS')
                else:
                    if mponderada >= 9:
                        print('Você tirou SS')

if mponderada >=5:
    print('Parabéns, você passou!')
else:
    print('Infelizmente você reprovou! :(')
