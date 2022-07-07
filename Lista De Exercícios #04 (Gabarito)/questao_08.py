cpf_input = input('\nInforme o CPF (somente os números): ')

if (len(cpf_input)!=11):
    print('\nQuantidade de dígitos inválida...\n')
else:
    # Formatando o CPF
    str_modelo = '\nCPF informado: {0}.{1}.{2}-{3}'
    print(str_modelo.format(cpf_input[0:3],cpf_input[3:6],cpf_input[6:9],cpf_input[9:11]))

    # Separando os 9 primeiros digitos dos 2 digitos verificadores
    cpf_parte_1 = cpf_input[:9]
    cpf_parte_2 = cpf_input[9:11]

    # validando o primeiro digito verificador
    multiplicador = 10
    cpf_digito_1  = 0
    posicao       = 0
    while posicao < len(cpf_parte_1):
        cpf_digito_1  += (int(cpf_parte_1[posicao]) * multiplicador)
        multiplicador -= 1
        posicao       += 1
    cpf_digito_1 = (cpf_digito_1 * 10) % 11
    if (cpf_digito_1 == 10): cpf_digito_1 = 0
    if (cpf_digito_1 != int(cpf_parte_2[0])):
        print('\nCPF Inválido...\n')
    else:
        # validando o segundo digito verificador
        multiplicador = 11
        cpf_digito_2  = 0
        posicao       = 0
        while posicao < len(cpf_parte_1):
            cpf_digito_2  += (int(cpf_parte_1[posicao]) * multiplicador)
            multiplicador -= 1
            posicao       += 1
        cpf_digito_2 += (cpf_digito_1 * 2)
        cpf_digito_2  = (cpf_digito_2 * 10) % 11
        if (cpf_digito_2 == 10): cpf_digito_2 = 0
        if (cpf_digito_2 != int(cpf_parte_2[1])):
            print('\nCPF Inválido...\n')
        else:
            print('\nCPF Válido...\n')
