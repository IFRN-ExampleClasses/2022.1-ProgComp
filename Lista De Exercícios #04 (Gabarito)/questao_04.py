texto = input('Digite um texto: ')

texto_invertido = ''

contador = 0
while contador < len(texto):
    texto_invertido = texto[contador] + texto_invertido
    contador += 1

print(f'\nO texto informado foi {texto.upper()}')
print(f'O texto invertido é {texto_invertido.upper()}')

if (texto.upper() == texto_invertido.upper()):
    print('\nO texto digitado é PALÍNDROMO...')
else:
    print('\nO texto digitado NÃO é PALÍNDROMO...')
