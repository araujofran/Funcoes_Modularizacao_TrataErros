import time
i=f=p=0
def voce(i,f,p):
    i=int(input('Inicio: '))
    f=int(input('Fim: '))
    p=int(input('Passo: '))
    print(20*'=-')
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i<f:
        c=i
        while c<=f:
            print(f'{c}s...',end='')
            if p<0:
                c-=p
            elif p>0:
                c+=p
            time.sleep(0.1)
        print()
    if i>f:
        c=i
        while c>=f:
            print(f'{c}s...',end='')
            if p>0:
                c-=p
            elif p<0:
                c+=p
            time.sleep(0.1)
        print()

print(20*'=-')
print('Contagem de 1 até 10 de 1 em 1')
c= 0
while c<10:
    print(f'{c+1}s... ',end='')
    time.sleep(0.1)
    c+=1
print()
print(20*'=-')
print('Contagem de 10 até 0 de 2 em 2')
c= 10
while c>=0:
    time.sleep(0.05)
    print(f'{c}s... ', end =' ')
    c-=2
print()
print(20*'=-')
print('Agora é a sua vez de personalizar a contagem!')
voce(i,f,p)
print(20*'=-')