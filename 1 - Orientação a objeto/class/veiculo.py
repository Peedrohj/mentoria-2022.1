from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict

@dataclass( frozen=True)
class Veiculo():
    velocidade: int = field(init=True, default=None)
    pk: int = field(init=True, default=None)
    modelo: str = field(init=True, default=None)
    cor: str = field(init=True, default=None)

class VeiculoRepositorio():
    def criarVeiculo(params: Dict):
        veiculo = Veiculo(**params)
        return veiculo
