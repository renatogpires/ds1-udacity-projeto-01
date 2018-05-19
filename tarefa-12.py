# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

def column_to_list(data, index):
    column_list = []
    controle = 0
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in data:
        column_list.append(data[controle][index])
        controle += 1
    return column_list

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = []

    for i in column_list:
        item_types.append(i)
        
    item_types = set(item_types)

    count_items = []
    male = 0
    female = 0
    unknown = 0

    for i in column_list:
        if i.strip() == "":
            unknown += 1
        elif i == "Male":
            male += 1
        else:
            female += 1
    
    count_items = [unknown, male, female]

    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------