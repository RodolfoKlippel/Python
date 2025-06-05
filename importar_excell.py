import csv

local_arquivo = "C:/Users/rodolfo.klippel/Desktop/arquivo_csv.csv"

lista=[["MUSTANG","FERRARI","LAMBORGHINI","BULGATI","LIMOUSINE"],
        [10000,15000,14000,20000,40000],
        [1,1,1,1,1]]

# Vertical (melhor)

with open(local_arquivo,"w") as arq:
    writer = csv.writer(arq,delimiter=";")
    for j in range(len(lista[0])):
        linha = [lista[0][j],lista[1][j],lista[2][j]]
        writer.writerow(linha)

# Horizontal

with open(local_arquivo,"w") as arq:
    writer = csv.writer(arq,delimiter=";")
    for j in range(len(lista)):
        writer.writerow(lista[j])

for i in range(len(lista[0])):
    for j in range(len(lista)):
        print(f"{lista[j][i]}",end=" ")
    print()