produtos =[]
qnt = []
preço = []
cont = 1
x = 0

while cont == 1: #Permite a entrada de dados pelo usuário
    p = input("Digite o nome do produto: ")
    q = input("Digite a quantidade: ")
    v = input("Digite o preço: ")

    if len(p)>0 and len(q)>0 and len(p)>0: #Confere se valores não estão vazios e os adiciona a lista
        produtos.append(p)
        qnt.append(q)
        preço.append(v)

        cont = int(input("Aperte 0 para parar ou 1 para adicionar mais produtos: "))
    else:
        print("Você precisa digitar todos os valores")

for i in produtos: #Mostra a lista separando-a em categorias
    print("Número / Produto / Quantidade / Preço")
    print(f"{x} - {produtos[x]} / {qnt[x]} / {preço[x]}R$")
    x += 1
