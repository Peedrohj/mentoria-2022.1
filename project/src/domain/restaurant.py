# Utils
from dataclasses import dataclass, field
from typing import Optional

# Domain
from .base_class import BaseClass


@dataclass(kw_only=True)
class Restaurant(BaseClass):
    name: str = field(init=True)
    url_image: str = field(init=True)
    address: str = field(init=True)
    description: Optional[str] = None
    is_active: Optional[bool] = True

    def __repr__(self) -> str:
        return f"{self.name} - {self.address}"
