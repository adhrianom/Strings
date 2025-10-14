frase = input().strip()

while frase != "*":
    palavras= frase.split()
    primeira_letra = palavras[0][0].lower()

    tautograma = all(p[0].lower() == primeira_letra for p in palavras)
    print("Y" if tautograma else "N")
    frase = input().strip()