n=5
vetor = [None]*n
soma= 0
print(f'Digite os {n} numeros: ')
for i in range (n):
    vetor[i] = int(input())
    soma= soma + vetor[i]
media = soma / n
print(f'média = {media}')
print(f'osnumero acima da media s]ao')
for e in vetor:
    if e > media:
        print(e)