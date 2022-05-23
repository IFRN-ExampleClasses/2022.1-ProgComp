# Programa para calcular a média e a frequência do IFRN

nota_1 = int(input('Informe a Nota da Etapa 1: '))
nota_2 = int(input('Informe a Nota da Etapa 2: '))

if nota_1>=0 and nota_1<=100 and nota_2>=0 and nota_2<=100:
    media = int((nota_1 * 2 + nota_2 * 3) / 5)
    qt_aulas  = int(input('Informe a Quantidade de Aulas: '))
    qt_faltas = int(input('Informe a Quantidade de Faltas: '))
    frequencia = int(100 - (qt_faltas / qt_aulas * 100))
    print(f'O Aluno obteve média = {media} e frequência = {frequencia}%')
else:
    print('ERRO: Informe notas entre 0 e 100...')
