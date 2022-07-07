frase_velha   = input('\nInforme a Frase: ').lower()
palavra_velha = input('\nProcurar.......: ').lower()
palavra_nova  = input('\nSubstituir por.: ').lower()

frase_nova = frase_velha.replace(palavra_velha, palavra_nova)

print(f'\n\n{frase_velha}')
print(f'\n{palavra_velha.upper()} foi substituida por {palavra_nova.upper()}')
print(f'\n{frase_nova}\n')
