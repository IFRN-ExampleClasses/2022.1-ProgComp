variavel      = '1234567890'
qt_caracteres = len(variavel)

posicao = 1
ida     = True
while True:
    print(variavel[0:posicao])
    if ida: 
        posicao += 1
        if posicao >= qt_caracteres: ida = False
    else:
        posicao -= 1
    if posicao < 1: break
