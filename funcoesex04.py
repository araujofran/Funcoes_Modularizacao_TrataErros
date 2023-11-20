'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

'''
def voto(ano):
    from datetime import date
    anoatual= date.today().year

    idade = anoatual - ano

    if idade <16:
        return f'Com {idade} anos ainda não tem idade para votar!!! '
    elif idade>=16 and idade <=17 or idade >70:
        return f'Com {idade} anos.Voto Facultativo!  ' 
    elif idade >17 and idade <=70:
        return f'Com {idade} anos. Voto Obrigatório!!! '
    
    print('FIM')

#Programa Principal
ano=int(input('Ano nascimento: '))
print(voto(ano))




