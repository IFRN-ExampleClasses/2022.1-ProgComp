import sys

texto = input('Digite algo: ')

print(texto)

tamanho_caracteres = len(texto) 
tamanho_memoria    = sys.getsizeof(texto)

print(tamanho_caracteres)
print(tamanho_memoria)