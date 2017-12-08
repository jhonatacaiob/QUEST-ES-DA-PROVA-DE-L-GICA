anoinicial = int(1995)
ano=int(input("QUAL O ANO?: "))
Porcentagem = 1.5/100
Salário=1000
while anoinicial<ano:
    Salário=Salário+(Salário*Porcentagem)
    Porcentagem *= 2
    anoinicial+=1
print("No ano de %i, ele irá receber %i" %(ano,Salário))
