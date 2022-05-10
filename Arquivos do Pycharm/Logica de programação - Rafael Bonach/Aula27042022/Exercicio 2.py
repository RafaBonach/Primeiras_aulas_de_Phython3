s = input('Digite uma sequencia de numeros ou letras: ')
t = len(s)
m = t // 2
novo = ' '
for ind in range(m):
    novo += (s[(t-1) - ind] + s[ind])

if t % 2 == 1:
    novo += s[m]

print(novo)