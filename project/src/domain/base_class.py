# Utils
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(kw_only=True)
class BaseClass:
    deleted_at: Optional[datetime] = field(default=None)
    updated_at: Optional[datetime] = field(default=None)
    created_at: datetime = field(
        default_factory=lambda: datetime.now())
