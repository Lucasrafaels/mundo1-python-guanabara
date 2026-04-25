dist = int(input('Qual a distância da sua viagem? '))
if dist <+ 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
    
print (f'A sua viagem custará R${preco:.2f}, tenha uma boa viagem!')
