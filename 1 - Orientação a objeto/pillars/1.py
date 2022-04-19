from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(kw_only=True, frozen=True)
class Veiculo():
    primary_key: int = field(init=True, default=0)
