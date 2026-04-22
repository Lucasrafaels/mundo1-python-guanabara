sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    novo_sal = sal + (sal*15/100)
else:
    novo_sal = sal + (sal*10/100)
print(f'O salário de R${sal:.2f} com o novo reajuste será de: R${novo_sal:.2f}')