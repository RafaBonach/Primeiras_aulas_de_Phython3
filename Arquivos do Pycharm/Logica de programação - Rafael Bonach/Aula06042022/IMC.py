print('Vamos calcular o seu IMC')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso
altura **=2
imc /=altura
print('O seu imc é ', '%.2f' % imc)
