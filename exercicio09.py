v = 0
s = 0
for x in range(10):
    n = float(input("Digite um número: "))
    if n < 0:
        v += 1
        print(n)
        s += n
p = 10 - v
if v == 0:
    print("Não existem números negativos")
elif v == 1:
    print(f"Existe apenas 1 número negativo")
else:
    print(f"{v} é a quantidade de números negativos e a soma deles é igual {s} e a quantidade de números positivos é {p}")
