while True:
    nota_1 = int(input('Informe a nota da Etapa 1 ..: '))
    nota_2 = int(input('Informe a nota da Etapa 2 ..: '))
    media = ((nota_1 * 2) + (nota_2 * 3)) / 5
    print(f'A Média foi {media}')
    continuar = input('Deseja Continuar (N para interromper)? ')
    if continuar == 'N' or continuar == 'n': break 

print('Fim do Programa...')