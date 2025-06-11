# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/album/

N = int(input())  # Total de figurinhas no álbum
M = int(input())  # Quantidade de figurinhas compradas

figurinhas = set()  # Conjunto para armazenar figurinhas únicas

for _ in range(M):
    x = int(input())  # Número da figurinha comprada
    figurinhas.add(x)  # Adiciona ao conjunto (não guarda duplicatas)

faltam = N - len(figurinhas)  # Quantas faltam
print(faltam)

# Esse deu trabalho hein, n lembrava do set()