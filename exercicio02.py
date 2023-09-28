h1 = int(input("Digite a hora: "))
m1 = int(input("Digite os minutos: "))
h2 = int(input("Digite a hora: "))
m2 = int(input("Digite os minutos: "))

if h1 > 12:
   h1 = h1-12

if h2 > 12:
    h2 = h2-12

sh = h1 + h2
sm = m1 + m2

if sm > 60:
    sh = sh + 1
    sm = sm - 60

if sh > 12:
    sh -= 12

if sm < 10:
    print(f"O resultado da soma é: {sh}:0{sm}")
else:
    print(f"O resultado da soma é: {sh}:{sm}")
