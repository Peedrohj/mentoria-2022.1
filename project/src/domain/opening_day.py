# Utils
from dataclasses import dataclass, field
from datetime import datetime

# Domain
from domain.object_values import Day

@dataclass(kw_only=True)
class OpeningDay:
    day: Day = field(init=True)
    opening_at : datetime = field(init=True)
    closing_at : datetime = field(init=True)
