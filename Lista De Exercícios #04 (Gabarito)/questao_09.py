PALAVRA_CHAVE = 'quadrilha'.upper()
palavra_info  = '_'*len(PALAVRA_CHAVE)
palavra_info = [*palavra_info]
erro = 0

while erro <=6:

    letra = input('Informe uma letra: ').upper()
    letra = letra.strip()
	
    if len(letra) > 1:
        print('Informe apenas 1 letra...\n')
        continue
    elif len(letra) < 1:
        print('Informe 1 letra...\n')
        continue
    
    if letra not in PALAVRA_CHAVE:
        erro += 1
        print(f'Voce informou a letra {letra}')
        print(f'Você errou {erro} vez(es)...\n')
        if erro == 6: break
        continue
    
    if letra in palavra_info:
        print(f'Você já informou essa letra...\n')
        continue

    posicao = 0
    while posicao < len(PALAVRA_CHAVE):
        if letra == PALAVRA_CHAVE[posicao]:
            palavra_info[posicao] = letra
        posicao += 1

    if "".join(palavra_info) == PALAVRA_CHAVE: break

    print(f'Você acertou....: {"".join(palavra_info)}\n')

if (erro == 6):
    print('\nInfelizmente você ENFORCADO!!!!')
    print(f'A PALAVRA-CHAVE era ............. {PALAVRA_CHAVE}\n')
else:
    print('\nParabéns, você ESCAPOU DA FORCA!!!!')
    print(f'A PALAVRA-CHAVE era .......... {PALAVRA_CHAVE}')
    print(f'Você informou a palavra ...... {"".join(palavra_info)}\n')
    