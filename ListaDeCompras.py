produtos =[]
qnt = []
preço = []
cont = 1
x = 0

while cont == 1:
    p = input("Digite o nome do produto: ")
    q = input("Digite a quantidade: ")
    v = input("Digite o preço: ")

    if len(p)>0 and len(q)>0 and len(p)>0:
        produtos.append(p)
        qnt.append(q)
        preço.append(v)

        cont = int(input("Aperte 0 para parar ou 1 para adicionar mais produtos: "))
    else:
        print("Você precisa digitar todos os valores")

for i in produtos:
    print("Número / Produto / Quantidade / Preço")
    print(f"{x} - {produtos[x]} / {qnt[x]} / {preço[x]}R$")
    x += 1
