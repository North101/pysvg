from dataclasses import dataclass

from ..attributes import (
    CoreAttributes,
    PresentationAttributes,
    StylingAttributes,
)
from ..attributes.presentation import d, placeholder
from .core import Element


@dataclass
class PathAttributes(CoreAttributes, StylingAttributes, PresentationAttributes):
  pathLength: int | None = None


class path(Element[PathAttributes]):
  element = 'path'
  attrs = PathAttributes
  d = d
  placeholder = placeholder
