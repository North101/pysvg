from typing import Literal, Union

from .base import Type

relative_units = Union[
    Literal['em'],
    Literal['ex'],
    Literal['ch'],
    Literal['rem'],
    Literal['vw'],
    Literal['vh'],
    Literal['vmin'],
    Literal['vmax'],
    Literal['%']
]
absolute_units = Union[
    Literal['px'],
    Literal['cm'],
    Literal['mm'],
    Literal['in'],
    Literal['pc'],
    Literal['pt']
]
units = relative_units | absolute_units


class length(Type):
  def __init__(self, value: float, unit: units | None = None):
    self.value = value
    self.unit: units | None = unit

  def __round__(self, ndigits=0):
    return length(round(self.value, ndigits), self.unit)

  def __format__(self, format_spec):
    return f'{self.value:{format_spec}}{self.unit if self.unit is not None else ''}'
