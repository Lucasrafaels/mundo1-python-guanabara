import math
ang = int (input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('O seno de {} é igual a: {:.2f}' .format(ang, seno))
print ('O cosseno de {} é igual a: {:.2f}' .format(ang, cos))
print ('A tangente de {} é igual a: {:.2f}' .format(ang,tan))