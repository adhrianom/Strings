gabarito = input()
prova_maria = input()

acertos = 0

for i in range(len(gabarito)):
    if gabarito[i] == prova_maria[i]:
        acertos += 1

print(acertos)

