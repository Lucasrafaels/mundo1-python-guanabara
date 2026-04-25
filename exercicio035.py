print ('Digite três seguimentos de reta para verificar se podem formar um triângulo')
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos escolhidos PODEM formar um triângulo')
else:
    print ('Os segmentos escolhidos NÃO PODEM formar um triângulo')