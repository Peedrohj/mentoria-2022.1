from dataclasses import dataclass, field


@dataclass()
class Veiculo:
    modelo: str
    cor: str
    __id: int = field(init=False)
    __velocidade: int = field(init=False, default=0)

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def id(self) -> int:
        return self.__id

    @velocidade.setter
    def velocidade(self, v: int) -> None:
        self._velocidade = v

carro: Veiculo =  Veiculo(modelo="Celta", cor="Preto")
carro.__id