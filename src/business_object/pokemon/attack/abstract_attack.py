from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def __init__(self, power=0, name=None, desc=None):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._power: int = power
        self._name: str | None = name
        self._desc: str | None = desc

    @abstractmethod
    def compute_damage(self, APkm1, APkm2) -> int:
        pass

    @property
    def power(self):
        return self._power

    @property
    def desc(self):
        return self._desc

    @property
    def name(self):
        return self._name
