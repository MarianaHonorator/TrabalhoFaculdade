
peso = float(input("Qual o peso do peixe ?"))


if peso > 50:
    excesso = peso - 50

else:
    excesso = 0


multa = excesso * 4

print(f'QUILO EXCEDENTE: {excesso} Kg')
print(f'VALOR DA MULTA: R$ {multa:.2f}')

