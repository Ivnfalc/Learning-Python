#Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: 
# uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. 
# como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar 
# se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos 
# valores de entrada todas as vezes que desejar.

def hora(h,m):
    b = h/12
    if b <= 1:
        hh= str(h)
        print('Sua hora: '+ hh + ':', end='')
    elif b>1 and b<2:
        hhh = str(h-12)
    else:
        print("formado de hora invalido")
    if b <= 1 and m <= 60:
        print(m, 'a.m')
    elif b > 1 and m <= 60:
        print(m, 'p.m')
    else:
        print('Formato de minutos invalidos')
while True:
    print('digite 666 para sair')
    h = int(input('Informe a hora:'))
    if h == 666:
        break
    m = int(input('Informe os minutos: '))
    hora(h, m)
