from dataclasses import dataclass

from ..attributes import (
    CoreAttributes,
    PresentationAttributes,
    StylingAttributes,
)
from ..types import length_percentage
from .core import Element


@dataclass
class CircleAttributes(CoreAttributes, StylingAttributes, PresentationAttributes):
  cx: length_percentage | None = None
  cy: length_percentage | None = None
  r: length_percentage | None = None
  pathLength: float | None = None


class circle(Element[CircleAttributes]):
  element = 'circle'
  attrs = CircleAttributes
