import math
cat1 = float(input('Qual o tamanho do cateto oposto? '))
cat2 = float(input('Qual o tamanho do cateto adjacente? '))
hipo =  math.hypot (cat1,cat2)
print ('A hipotenusa será: {:.2f}' .format(hipo))