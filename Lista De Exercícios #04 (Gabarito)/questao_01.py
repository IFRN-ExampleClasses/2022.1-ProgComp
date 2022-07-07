# Garantir que todas as vogais acentuadas estão nessa variável
vogais = 'AEIOUÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜ'

variavel = input('Digite algo: ')

conta_vogal = 0
posicao     = 0
while posicao < len(variavel):
    if variavel[posicao].upper() in vogais: conta_vogal += 1
    posicao += 1

print(f'\nO que você digitou possui {conta_vogal} vogais\n')