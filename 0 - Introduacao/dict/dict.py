from typing import Dict, List

# Exemplo básico de dicionário
dicionario_de_pessoas: Dict = {
    "Andre": {
        "idade": 12
    },
    "Luciana": {
        "idade": 21
    }
}

# Adicinoar um elemento ao dicionário
dicionario_de_pessoas["Pedro"] = {"idade": 21}
{'Andre': {'idade': 12}, 'Luciana': {'idade': 21}, 'Pedro': {'idade': 21}}

# Atualizar um elemento do dicionário
dicionario_de_pessoas["Pedro"]["idade"] = 22
{'Andre': {'idade': 12}, 'Luciana': {'idade': 21}, 'Pedro': {'idade': 22}}

# Buscar um elemento no dicionário
dicionario_de_pessoas["Pedro"]
{'idade': 22}

dicionario_de_pessoas.get("Pedro")
{'idade': 22}

# Remover um elemento do dicionário
del dicionario_de_pessoas["Pedro"]
{'Andre': {'idade': 12}, 'Luciana': {'idade': 21}}

pedro = dicionario_de_pessoas.pop("Pedro")
# OBS: Essa função retira o elemento e retornar ele, ou seja o output
# vai ser {'idade': 21} mas no dicionário não terá mais a pessoa Pedro

# Retorna o último elemento e remove ele do dicionário
pedro = dicionario_de_pessoas.popitem()

# Buscar as chaves do dicionário
dicionario_de_pessoas.keys()

# Buscar as valores do dicionário
dicionario_de_pessoas.values()
