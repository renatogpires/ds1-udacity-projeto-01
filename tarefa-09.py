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

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    controle = 0
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in data:
        column_list.append(data[controle][index])
        controle += 1
    return column_list

# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = float(trip_duration_list[1])
max_trip = float(trip_duration_list[1])
mean_trip = 0.
median_trip = 0.


# Cálculo de min_trip
for i in trip_duration_list:
    if float(i) < min_trip:
        min_trip = float(i)
    
# Cálculo de max_trip
for i in trip_duration_list:
    if float(i) > max_trip:
        max_trip = float(i)

# Cálculo de mean_trip
for i in trip_duration_list:
    mean_trip = mean_trip + float(i)

mean_trip = mean_trip / len(trip_duration_list)

# Cálculo de median_trip
quantidade = len(trip_duration_list)
new_trip_duration_list = []

for i in trip_duration_list:
    new_trip_duration_list.append(float(i))
trip_duration_list = sorted(new_trip_duration_list)

mod = quantidade % 2

if mod != 0:
    meio = (quantidade // 2)
    median_trip = trip_duration_list[meio]
else:
    meio = (quantidade // 2)
    median_trip = (float(trip_duration_list[meio - 1]) + float(trip_duration_list[meio])) / 2

min_trip = round(min_trip)
max_trip = round(max_trip)
mean_trip = round(mean_trip)
median_trip = round(median_trip)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------