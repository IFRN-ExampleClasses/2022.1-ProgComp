'''
6.	Faça um programa que receba uma palavras e imprima essa palavra na vertical (em escada).
Exemplo: Ao ser informada a palavra NATAL, o programa imprime conforme poder ser visto abaixo:
'''

texto = input('Digite um texto: ')

contador = 1

while contador <= len(texto):
    print(texto[0:contador])
    contador += 1
    