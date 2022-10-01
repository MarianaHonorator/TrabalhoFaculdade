import math

med = float(input("Qual o tamanho em metros quadrados da área ?"))
#litros necessarios: 
litros = med/6
#10% de folga na mistura:
litros_folga = litros * 1.1
latas = litros/18
galao = litros/3.6

#latas:
if latas % 18 != 0:
    latas +=1
    preco_lata = math.floor(latas) * 80
#galões:
if galao % 3.6 != 0:
    galao += 1
    preco_galao = math.floor(galao) * 25

#mistura:
mistura_lata = int(litros_folga/18)
mistura_galao = int((litros_folga - (mistura_lata * 18)) / 3.6)

if litros_folga - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print("Você tem 3 opções:\n")
print(f'1. Comprar {math.floor(latas)} lata(s) de 18 litros por R$ {preco_lata}')
print(f'2. Comprar {math.floor(galao)} galão(s) de 3.6 litros por R$ {preco_galao}')
print(f'3. Comprar {mistura_lata} lata(s) de 18 litros e {mistura_galao} galão(s) de 3.6 litros por R$ {mistura_lata * 80 + mistura_galao * 25}')
