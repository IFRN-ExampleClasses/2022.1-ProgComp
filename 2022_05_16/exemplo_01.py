# Exemplo do Slide 36 das Notas de Aula #03

teste = False

# --------------------------------------------------
# Variáveis - Situação 1
a = 3
b = 16
nome = 'MIRIAM'
profissao = 'ADVOGADO'

a1 = (a + 1 >= ((b)**(1/2))) or (nome != 'ANA')
b1 = (a + 1 >= ((b)**(1/2))) and (profissao == 'MEDICO')
c1 = (nome != 'ANA') or (profissao == 'MEDICO') and (a + 1 >= ((b)**(1/2)))
d1 = not teste and (a + 1 >= ((b)**(1/2))) or not (profissao == 'MEDICO')
e1 = not ((a + 1 >= ((b)**(1/2))) and teste)

# --------------------------------------------------
# Variáveis - Situação 2
a = 5
b = 64
nome = 'PEDRO'
profissao = 'MEDICO'

a2 = (a + 1 >= ((b)**(1/2))) or (nome != 'ANA')
b2 = (a + 1 >= ((b)**(1/2))) and (profissao == 'MEDICO')
c2 = (nome != 'ANA') or (profissao == 'MEDICO') and (a + 1 >= ((b)**(1/2)))
d2 = not teste and (a + 1 >= ((b)**(1/2))) or not (profissao == 'MEDICO')
e2 = not ((a + 1 >= ((b)**(1/2))) and teste)

# --------------------------------------------------
# Variáveis - Situação 3
a = 2.5
b = 9
nome = 'ANA'
profissao = 'PROFESSOR'

a3 = (a + 1 >= ((b)**(1/2))) or (nome != 'ANA')
b3 = (a + 1 >= ((b)**(1/2))) and (profissao == 'MEDICO')
c3 = (nome != 'ANA') or (profissao == 'MEDICO') and (a + 1 >= ((b)**(1/2)))
d3 = not teste and (a + 1 >= ((b)**(1/2))) or not (profissao == 'MEDICO')
e3 = not ((a + 1 >= ((b)**(1/2))) and teste)

# Imprimindo os resultados
print(f'01) {a1} - {b1} - {c1} - {d1} - {e1}')
print(f'02) {a2} - {b2} - {c2} - {d2} - {e2}')
print(f'03) {a3} - {b3} - {c3} - {d3} - {e3}')
print(' ')
print('01)', a1, '-', b1, '-', c1, '-', d1, '-', e1)
print('02)', a2, '-', b2, '-', c2, '-', d2, '-', e2)
print('03)', a3, '-', b3, '-', c3, '-', d3, '-', e3)