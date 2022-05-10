nota1 = float(input('Digite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))
media = (nota1 + nota2)/2
if media >= 5:
    print(f'Você está APROVADO. Sua média foi {media} e a nota minima para passar é 5')
else:
    print(f'Infelizmente você está REPROVADO. Sua média foi {media} e a nota minima para passar é 5')
