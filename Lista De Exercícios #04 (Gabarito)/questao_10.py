# Solicitando os dados de entrada
coord_X_ini = int(input('Informe a Coordenada X: '))
coord_Y_ini = int(input('Informe a Coordenada Y: '))
mov_lido    = input('Informe a sequência de Movimentação: ').upper()
print('='*80)

# Calculando o quadrante inicial
if   (coord_X_ini > 0)  and (coord_Y_ini > 0) : quadrante_inicial = '1º Quadrante'
elif (coord_X_ini < 0)  and (coord_Y_ini > 0) : quadrante_inicial = '2º Quadrante'
elif (coord_X_ini < 0)  and (coord_Y_ini < 0) : quadrante_inicial = '3º Quadrante'
elif (coord_X_ini > 0)  and (coord_Y_ini < 0) : quadrante_inicial = '4º Quadrante'
elif (coord_X_ini > 0)  and (coord_Y_ini == 0): quadrante_inicial = 'Eixo X (Positivo)'
elif (coord_X_ini < 0)  and (coord_Y_ini == 0): quadrante_inicial = 'Eixo X (Negativo)'
elif (coord_X_ini == 0) and (coord_Y_ini > 0) : quadrante_inicial = 'Eixo Y (Positivo)'
elif (coord_X_ini == 0) and (coord_Y_ini < 0) : quadrante_inicial = 'Eixo Y (Negativo)'
else: quadrante_inicial = 'Origem do Plano Cartesiano'

# Calculando a movimentação do Robô
coord_X_fim = coord_X_ini
coord_Y_fim = coord_Y_ini
mov_validos = ''

#for posicao in movimentos:
posicao = 0
while posicao < len(mov_lido):
   movimento = mov_lido[posicao]
   if movimento not in 'UDRLONEW': 
      posicao += 1
      continue
   mov_validos = mov_validos + movimento
   if   (movimento == 'U'): # para cima
      coord_Y_fim += 1
   elif (movimento == 'D'): # para baixo
      coord_Y_fim -= 1
   elif (movimento == 'R'): # para a direita
      coord_X_fim += 1
   elif (movimento == 'L'): # para a esquerda
      coord_X_fim -= 1
   elif (movimento == 'O'): # para cima e esqueda
      coord_Y_fim += 1
      coord_X_fim -= 1
   elif (movimento == 'N'): # para cima e direita
      coord_Y_fim += 1
      coord_X_fim += 1
   elif (movimento == 'E'): # para baixo e direita
      coord_Y_fim -= 1
      coord_X_fim += 1
   elif (movimento == 'W'): # para baixo e esquerda
      coord_Y_fim -= 1
      coord_X_fim -= 1
   posicao += 1

# Calculando o quadrante final
if   (coord_X_fim > 0)  and (coord_Y_fim > 0) : quadrante_final = '1º Quadrante'
elif (coord_X_fim < 0)  and (coord_Y_fim > 0) : quadrante_final = '2º Quadrante'
elif (coord_X_fim < 0)  and (coord_Y_fim < 0) : quadrante_final = '3º Quadrante'
elif (coord_X_fim > 0)  and (coord_Y_fim < 0) : quadrante_final = '4º Quadrante'
elif (coord_X_fim > 0)  and (coord_Y_fim == 0): quadrante_final = 'Eixo X (Positivo)'
elif (coord_X_fim < 0)  and (coord_Y_fim == 0): quadrante_final = 'Eixo X (Negativo)'
elif (coord_X_fim == 0) and (coord_Y_fim > 0) : quadrante_final = 'Eixo Y (Positivo)'
elif (coord_X_fim == 0) and (coord_Y_fim < 0) : quadrante_final = 'Eixo Y (Negativo)'
else: quadrante_final = 'Origem do Plano Cartesiano'

# Exibindo os resultados finais
print(f'\nPosição Inicial do Robô ............: ({coord_X_ini},{coord_Y_ini})')
print(f'Quadrante Inicial do Robô ..........: {quadrante_inicial}')
print(f'Sequência de Movimentos Informados .: {mov_lido}\n')
print(f'Sequência de Movimentos Válidos ....: {mov_validos}')
print(f'Quantidade de Movimentos Realizados : {len(mov_validos)}')
print(f'Posição Final do Robô ..............: ({coord_X_fim},{coord_Y_fim})')
print(f'Quadrante Final do Robô ............: {quadrante_final}\n')
