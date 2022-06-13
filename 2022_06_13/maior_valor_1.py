'''
Faça um programa em Python que leia n números inteiros e positivos 
a partir do teclado, até que o usuário digite 0. 
Ao final, informe o maior número digitado.
'''

maior = 0
while True:
    valor = int(input('Informe um valor inteiro positivo: '))

    if valor == 0:
        break
    elif valor < 0:
        print('ERRO: Informe apenas valores POSITIVOS...')
        continue

    # Descobrir o maior número
    if (valor > maior):
        maior = valor
        print(f'O maior valor foi substituido por {maior}')
    else:
        print(f'O maior valor continua sendo {maior}')

print(f'O maior valor digitado foi {maior}')