import sys

valor_1   = 1500000009999
tamanho_1 = sys.getsizeof(valor_1)
tipo_1    = type(valor_1)
print(f'A variavel VALOR_1 é do tipo {tipo_1} e ocupa {tamanho_1} bytes em memória')

valor_2   = '10'
tamanho_2 = sys.getsizeof(valor_2)
tipo_2    = type(valor_2)
print(f'A variavel VALOR_2 é do tipo {tipo_2} e ocupa {tamanho_2} bytes em memória')

