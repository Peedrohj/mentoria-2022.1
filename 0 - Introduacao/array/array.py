from typing import List

# Exemplo básico de lista
lista_de_numeros: List[int] = [1, 2, 3, 3, 4, 5]
lista_de_strings: List[str] = ["a", "b", "c", "d", "e"]
lista_de_objetos: List[dict] = [{
    "nome": "Andre",
    "idade": 12
}, {
    "nome": "Luciana",
    "idade": 51
}]
lista_de_lista: List[List] = [[1, 2, 3, 3, 4, 5],
                  ["a", "b", "c", "d", "e"]]

# Adicinoar um elemento ao final da lista
lista_de_numeros.append(6)
[1, 2, 3, 3, 4, 5, 6]

# Adicinoar um elemento a uma posição da lista
lista_de_numeros.insert(0, 6)
[6, 1, 2, 3, 3, 4, 5]

# Remover um item da lista
# OBS: Essa função vai remover apenas a primera ocorrência
lista_de_numeros.remove(1)
[2, 3, 3, 4, 5]

# Remover o último elemento da lista
lista_de_numeros.pop()
[1, 2, 3, 3, 4]

# Remover um elemento pelo index
lista_de_numeros.pop(1)
[1, 3, 3, 4, 5]
