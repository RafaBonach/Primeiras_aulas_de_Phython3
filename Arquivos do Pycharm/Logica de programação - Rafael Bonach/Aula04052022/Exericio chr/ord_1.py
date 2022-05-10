print('Criptografias de codigos')
cod = input('Digite o valor a ser codificado: ')

if (cod==''):
    print("informe uma frase, pro favor")
else:
    cesar=" "
    for car in cod:
        cesar += chr(ord(car) + 1)
    print(cesar)
    qtd = cesar//2