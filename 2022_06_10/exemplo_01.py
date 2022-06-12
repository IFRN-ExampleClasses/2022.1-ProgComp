base     = int(input('Informe o valor da base: '))
expoente = int(input('Informe o valor do expoente: '))

resultado = 1
contador  = 1

while contador <= expoente:
    resultado = resultado * base
    #resultado *= base
    contador  = contador + 1
    #contador += 1

print(resultado)