print(' == Calculadora de frete == ')
pesoc = float(input('Digite quantas toneladas o motorista levou: '))
valorf = float(input('Digite o valor fixo por tonelada: '))
dieselg = float(input('Digite o total de KMs percorridos: '))
distp = float(input('Digite o preço por KM: '))
totall = pesoc * valorf
totald = dieselg * distp
print('O total foi de R${:.2f}!'.format(totall))
print('O gasto total em Diesel foi de {:.2f}'.format(totald))
apagar = totall - totald
print('Com o desconto do Diesel, voce deverá pagar a quantia de {} ao motorista.'.format(apagar))
