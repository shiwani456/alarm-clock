from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Alarm:
    id: int
    time: str
    label: str
    repeat: bool = False
    enabled: bool = True

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        status = "ON" if self.enabled else "OFF"
        repeat = "Daily" if self.repeat else "Once"

        return (
            f"[{self.id}] "
            f"{self.time} | "
            f"{repeat} | "
            f"{status} | "
            f"{self.label}"
        )