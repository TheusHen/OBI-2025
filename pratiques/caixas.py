# https://olimpiada.ic.unicamp.br/pratique/pj/2020/f1/caixas/

A = int(input())
B = int(input())
C = int(input())

if A + B < C:
    print(1)
elif A < B and B < C:
    print(1)
elif A < B or A < C or B < C:
    print(2)
else:
    print(3)