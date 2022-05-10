#ni = numero inicial
#nf = numero final
#p = passo
ni = int(input('Digite o número inicial: '))
nf = int(input('Digite o número final: '))

if nf<=ni:
    print('O numero inicial deve ser maior que o final')
    exit(0)

p = int(input('Digite o passo: '))
if p <=0:
    print('Digite um passo positivo')
    exit(0)
for contagem in range(ni, nf, p):
    if contagem + p == nf:
        print(' e ', end='')
    else:
        print(',', end='')
    print(contagem, end='')
