from dataclasses import dataclass
from typing import Literal

from .base import Attributes

none = Literal['none']
auto = Literal['auto']
inherit = Literal['inherit']


@dataclass
class XmlNamespace(Attributes):
  base: str | None = None
  lang: str | None = None
  space: Literal['default'] | Literal['preserve'] | None = None


@dataclass
class CoreAttributes(Attributes):
  id: str | None = None
  lang: str | None = None
  tabindex: int | None = None
  xml: XmlNamespace | None = None
