from dataclasses import dataclass

from ..attributes import (
    CoreAttributes,
    PresentationAttributes,
    StylingAttributes,
    auto,
)
from ..types import length_percentage
from .core import Element


@dataclass
class CircleAttributes(CoreAttributes, StylingAttributes, PresentationAttributes):
  x: length_percentage | None = None
  y: length_percentage | None = None
  width: auto | length_percentage | None = None
  height: auto | length_percentage | None = None
  rx: auto | length_percentage | None = None
  ry: auto | length_percentage | None = None
  pathLength: float | None = None


class rect(Element[CircleAttributes]):
  element = 'rect'
  attrs = CircleAttributes
