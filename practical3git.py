print('introdueix un numero')
numero = input()
numero = int(numero)
contador = 1
total_numeros_div3 = 0
while contador < numero:
    if contador % 3 == 0:
        total_numeros_div3 = total_numeros_div3 + 1
        print(contador)
    contador = contador + 1
print('hi ha un total de', total_numeros_div3, 'numeros divisibles entre 3')
