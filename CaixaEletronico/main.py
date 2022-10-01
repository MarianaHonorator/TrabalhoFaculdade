import math
print("Saque de 10 a 600 reais")
saque = int(input("Digite o valor do saque: "))

#NOTAS DE 1 A 100
notacem = math.floor(saque/100)
notacinq = math.floor((saque % 100)/50)
notadez = math.floor(((saque % 100) % 50)/10)
notacinco =math.floor((((saque % 100) % 50) % 10)/5)
notaum = math.floor(((((saque % 100) % 50) % 10) % 5)/1)

print("\nVocê recebera as seguintes notas:\n")
print(f'{notacem} nota(s) de 100')
print(f'{notacinq} nota(s) de 50')
print(f'{notadez} nota(s) de 10')
print(f'{notacinco} nota(s) de 5')
print(f'{notaum} nota(s) de 1')