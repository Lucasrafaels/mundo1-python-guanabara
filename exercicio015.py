km = float (input('Quantos km foram percorridos? '))
dias = int (input('Por quantos dias ele foi alugado? '))
total = (km * 0.15) + (dias * 60)
print ('Você deverá pagar {:.2f} R$ pelo aluguel total do veículo' .format(total))