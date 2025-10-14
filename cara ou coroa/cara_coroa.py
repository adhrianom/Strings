num_partidas = int(input())
maria = 0
joao = 0
## 0 Maria venceu, 1 João venceu

while num_partidas > 0:
    partida = input().split()
    for valor in partida:
        if valor == "0":
            maria += 1
        else:
            joao += 1
    print(f"Mary won {maria} times and John won {joao} times")
    maria = 0
    joao = 0
    num_partidas = int(input())

