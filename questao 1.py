palavra = input("Digite uma Palavra: ").lower()
palavra_invertida = ""
if " " in palavra:
    print("DIGITE UMA PALAVRA")
else:
    for l in range(len(palavra)-1,-1,-1):
        palavra_invertida+=palavra[l]
    if palavra_invertida==palavra:
        print("ISSO É UMA PALÍNDROMA")
    else:
        print("ISSO NÃO É UMA PALÍNDROMA")
