def dv_correto(numero: str):
    soma = 0
    peso = len(numero)
    for i in range(len(numero)-1):
        soma += int(numero[i]) * peso
        peso -= 1
    dv = 11 - soma % 11
    if dv >= 10:
        dv = 0

    return dv == int(numero[-1])


cpf = input()
cpf = cpf.replace(".", "").replace("-", "").strip()

eh_valido = len(cpf) == 11 and dv_correto(cpf) and dv_correto(cpf[:-1]) and  cpf.count(cpf[0]) != 11

print(eh_valido)