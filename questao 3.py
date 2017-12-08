damasceno = [0,1]
n = int(input("Digite um Numero: "))
while len(damasceno)<n:
    numero = (damasceno[-1]*damasceno[-2])+1
    damasceno+=[numero]
jo = " ".join(damasceno)
print("A SEQUENCIA É", damasceno)
