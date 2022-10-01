
peso = float(input("Qual o peso do peixe ?"))

#caso peso passe de 50kg:
if peso > 50:
    excesso = peso - 50
#caso não passe:
else:
    excesso = 0

#multa referente ao excesso
multa = excesso * 4

print(f'QUILO EXCEDENTE: {excesso} Kg')
print(f'VALOR DA MULTA: R$ {multa:.2f}')

