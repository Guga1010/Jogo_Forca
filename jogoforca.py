import os
os.system("cls")

acertou = False
acertos = 0
chances = 5
palavra = input("Peça ao seu amigo tampar os olhos e digite a palavra: ")
os.system("cls")
tam = len(palavra)
pal_ocl  = ["-"] * tam

while chances > 0 and acertos < tam:
    i = 0
    print("Palavra: "+ str(pal_ocl))
    print("Chances: "+str(chances))
    letra = input("Digite uma letra: ")
    for x in palavra:
        if letra == x:
            pal_ocl[i] = x
            acertos+=1
            acertou = True
        i+=1
    if not acertou:
        chances -=1
    acertou = False
    os.system("cls")

    

print("Palavra oculta: "+palavra+", chances: "+str(chances))
if chances == 0:
    print("Você perdeu")
else:
    print("Você ganhou")
