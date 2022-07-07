# Informando as 2 palavras
texto_1 = input('Informe a 1ª Palavra: ')
texto_2 = input('Informe a 2ª Palavra: ')

# Removendo os espaços a direita e a esquerda da palavra
texto_1 = texto_1.strip()
texto_2 = texto_2.strip()

# Uniformizando as duas palavras para minúsculas
texto_1 = texto_1.lower()
texto_2 = texto_2.lower()

if sorted(texto_1) == sorted(texto_2):
    print('As palavras são Anagramas...')
else:
    print('As palavras não são Anagramas...')