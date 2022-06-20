captcha = '6hYt8G'

print(captcha)
texto = input('\nInforme o Captcha: ')

captcha = captcha.upper()
texto   = texto.upper()

if (texto == captcha):
    print('OK...')
else:
    print('ERRO...')