from dataclasses import dataclass
from typing import Literal, Sequence, Union

from ..attributes import (
    CoreAttributes,
    PresentationAttributes,
    StylingAttributes,
)
from ..types import length_percentage
from .core import Element


@dataclass
class TextAttributes(CoreAttributes, StylingAttributes, PresentationAttributes):
  x: length_percentage | None = None
  y: length_percentage | None = None
  dx: length_percentage | None = None
  dy: length_percentage | None = None
  rotate: Sequence[float] | None = None
  lengthAdjust: Literal['spacing'] | Literal['spacingAndGlyphs'] | None = None
  textLength: length_percentage | None = None

  text_anchor: Union[
      Literal['start'],
      Literal['middle'],
      Literal['end'],
  ] | None = None

  font_family: str | None = None
  font_size: length_percentage | None = None
  font_style: Literal['normal'] | Literal['italic'] | Literal['oblique'] | None = None
  font_weight: Union[
      Literal['normal'],
      Literal['bold'],
      Literal['bolder'],
      Literal['lighter'],
      float,
      None,
  ] = None


class text(Element[TextAttributes]):
  element = 'text'
  attrs = TextAttributes
