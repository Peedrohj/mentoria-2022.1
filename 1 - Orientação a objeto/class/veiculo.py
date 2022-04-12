from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(kw_only=True, frozen=True)
class BaseClass:
    def set(self, nome: str, value: any):
        object.__setattr__(self, nome, value)


@dataclass(kw_only=True, frozen=True)
class Veiculo(BaseClass):
    velocidade: int = field(init=True, default=None)
    acelaracao: int = field(init=True, default=None)

    id: int = field(init=True, default=None)
    modelo: str = field(init=True, default=None)
    cor: str = field(init=True, default=None)

    def atualizarModelo(self, value):
        self.set(nome="modelo", value=value)

carro: Veiculo = Veiculo(modelo="Celta", cor="Preto", velocidade=10, id=1)
carro.atualizarModelo("Gol")
carro.velocidade
carro.id
carro.modelo