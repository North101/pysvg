from dataclasses import dataclass
from typing import Sequence

from .base import Attributes


@dataclass
class StylingAttributes(Attributes):
  class_: str | Sequence[str] | None = None
  style: str | Sequence[str] | None = None
