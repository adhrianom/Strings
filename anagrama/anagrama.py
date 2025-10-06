p1 = input()
p2 = input()

anagrama = len(p1) == len(p2) and p1 != p2

for letra in p1:
    if p1.count(letra) != p2.count(letra):
        anagrama = False
        break
    
print(anagrama)