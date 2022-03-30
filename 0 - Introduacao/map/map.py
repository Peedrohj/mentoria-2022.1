from typing import List, Dict

# Exemplo básico de uso de Map para lista
lista_de_nomes: List[str] = ["Marcelo", "Caio", "Ester", "Manuela"]
lista_de_numeros: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

nomes_maisculos: List[str] = list(
    map(lambda nome: nome.upper(), lista_de_nomes))
numeros_ao_quadrado: List[int] = list(
    map(lambda numero: numero * 2, lista_de_numeros))
