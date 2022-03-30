from typing import List, Dict

# Exemplo básico de uso de filter para lista
lista_de_nomes = ["Marcelo", "Caio", "Ester", "Manuela"]
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def nomes_com_m(nome: str) -> bool:
    return bool((nome.lower().startswith("m")))

# Filtros
nomes_que_comecam_com_m = filter(nomes_com_m, lista_de_nomes)
numeros_pares = filter(lambda numero: numero % 2 == 0, lista_de_numeros)

# Procurando a primeira ocorrência
numero_2 = next(iter(numeros_pares))