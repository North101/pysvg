from dataclasses import dataclass

from ..attributes import (
    CoreAttributes,
    PresentationAttributes,
    StylingAttributes,
)
from .core import Element


@dataclass
class GAttributes(CoreAttributes, StylingAttributes, PresentationAttributes):
  pass


class g(Element[GAttributes]):
  element = 'g'
  attrs = GAttributes
