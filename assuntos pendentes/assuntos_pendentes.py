entrada = input().strip()

pilha = 0
pendente = False

for c in entrada:
    if c == "(":
        pilha += 1
    elif c == ")":
        pilha -= 1
        if pilha < 0:
            pendente = True
            break
if pilha != 0:
    pendente = True

if pendente:
    print(f"Ainda temos {abs(pilha)} assunto(s) pendente(s)!")
else:
    print("Partiu RU!")
