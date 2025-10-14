n_nomes = int(input())
nomes = []

for _ in range(n_nomes):
    nomes.append(input())

maria_count = 0
for nome in nomes:
    palavras = nome.split()
    maria_count += palavras.count("Maria")

print(maria_count)
