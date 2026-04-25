velocidade = int(input('Digite a velocidade do veículo: '))
multa = (velocidade - 80) * 7
if velocidade < 80:
    print('Você está dirigindo na velocidade correta, tenha um bom dia!')
else:
    print ('MULTADO, o limite da via é 80km/h e você estava a {}Km/h, por isso receberá uma multa de R${:.2f}!' .format(velocidade, multa))