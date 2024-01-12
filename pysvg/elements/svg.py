from dataclasses import dataclass

from ..attributes import CoreAttributes, PresentationAttributes, StylingAttributes
from ..types import length_percentage
from .core import Element


@dataclass
class SVGAttributes(CoreAttributes, StylingAttributes, PresentationAttributes):
  xmlns: str = 'http://www.w3.org/2000/svg'
  baseProfile: str | None = None
  preserveAspectRatio: str | None = None
  version: float | None = None
  viewBox: tuple[float, float, float, float] | None = None
  width: length_percentage | None = None
  height: length_percentage | None = None
  x: length_percentage | None = None
  y: length_percentage | None = None


class svg(Element[SVGAttributes]):
  element = 'svg'
  attrs = SVGAttributes
