def mensagem(msg):
    traçoscont=0
    while traçoscont<(len(msg)):
        traçoscont+=1
    t=traçoscont
    c=0
    while c<t:
        print('=',end='')
        c+=1
    print()
    print(msg)
    c=0
    while c<t:
        print('=',end='')
        c+=1
    print()


r='S'
while r=='S':
    msg=str(input('Mensagem: ')).strip().upper()
    mensagem(msg)
    
    r= str(input('Quer continuar?[S/N] ')).strip().upper()

    if r == 'Nn': 
        break
print()
print('FIM DO TESTE! Obrigado! \n')