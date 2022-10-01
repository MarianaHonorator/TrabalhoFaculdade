gph = float(input("Quanto você ganha por hora?"))
htm = int(input("Quantas horas trabalhadas no mês?"))

SalarioBruto = htm * gph
#Descontos:
IR = SalarioBruto * 0.11
sdt = SalarioBruto * 0.05
inss = SalarioBruto * 0.08
Descontos = IR + sdt + inss
#Salário Líquido:
SalarioLiq = SalarioBruto - Descontos

print(f'+ Salário Bruto : R$ {SalarioBruto:.2f} ')
print(f'- IR (11%) : R$ {IR:.2f} ')
print(f'- INSS (8%) : R$ {inss:.2f} ')
print(f'- Sindicato (5%) : R$ {sdt:.2f} ')
print(f'= Salário Liquido : R$ {SalarioLiq:.2f} ')
