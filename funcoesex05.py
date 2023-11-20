def fat(num,show=True):
    """
    -> Calcula o fatorial de um número:
    :param num: O número a ser calculado.
    : para show:(opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um numero num.
    """

    f=1
    for c in range(num,0,-1):
        if show:
            print (c, end=' ')
            if c>1:
                print('x',end=' ')
            else:
                print('=',end=' ')
        f*=c
    return f
    print()

#Programa Principal

num = int(input('Digite o número: '))
print (fat(num))
help(fat)