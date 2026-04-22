a = int(input('Digite um valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
menor = a
maior = a
if b < menor:
    menor = b
if c < menor:
    c = menor
if b > maior:
    b = maior
if c > maior:
    menor = c
print(f'O maior número digitado foi: {maior} e o menor número digitado foi: {menor}')