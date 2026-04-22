alt = float (input('Altura da parede: '))
larg = float (input('Largura da parede: '))
area = alt*larg
tinta = area/2
print ('A área da sua parede é igual a {:.2f}m²' .format(area))
print ('Você precisará de {:.2f} litros de tintas para pintar essa parede' .format(tinta))