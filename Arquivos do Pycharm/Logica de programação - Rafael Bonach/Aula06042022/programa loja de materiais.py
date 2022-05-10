print('Desconto que deve ser aplicado na compra')
print()
valor=float(input('Digite o valor que será dado o desconto: R$ '))
porcentagem = float(input('Digite o valor do desconto: '))
desconto = valor
desconto *= porcentagem
desconto /=100
resultante = valor
resultante -= desconto
print()
print('O valor total é R$', valor,'e o valor com desconto é R$', resultante)