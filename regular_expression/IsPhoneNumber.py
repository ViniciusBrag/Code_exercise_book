def isPhoneNumber(text):
    #u: valida o tamanho(len) padrão americano
    if len(text) != 12:
        return False

    #v: verifica entre os (3) primeiros números é decimal 
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    #w: verifica se no indice[3] existe um '-' - hifén
    if text[3] != '-':
        return False 

    #x: verifica entre os ([4] a [7] = 3) números é decimal 
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    #y: verifica se no indice[7] existe um '-' - hifén
    if text[7] != '-':
        return False

    #z: #x: verifica entre os ([8] a [12] = 4) números é decimal 
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f'Phone number found {chunk}')
print('Done')
        