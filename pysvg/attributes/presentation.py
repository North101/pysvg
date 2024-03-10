from dataclasses import dataclass
from functools import reduce
from typing import Callable, Literal, Sequence

from ..types import color, length_percentage, percentage, transform
from .base import Attribute, Attributes
from .core import auto, inherit, none


class DrawSegment:
  def __neg__(self):
    raise NotImplementedError()

  @property
  def rel_x(self):
    return 0

  @property
  def rel_y(self):
    return 0

  def abs_x(self, x: float):
    return x + self.rel_x

  def abs_y(self, y: float):
    return y + self.rel_y

  def placeholder(self, width: float, height: float) -> 'DrawSegment':
    return self


class d(Attribute, DrawSegment):
  sep = ' '

  def __init__(self, value: Sequence[DrawSegment]):
    self.value = value

  def __format__(self, format_spec):
    value = (
        f'{value:{format_spec}}'
        for value in self.fill_placeholders.flat_values
    )
    return f'{self.sep.join(value)}'

  def __add__(self, other: 'd'):
    return d([*self.value, *other.value])

  def __sub__(self, other: 'd'):
    return self + -other

  def __neg__(self):
    return d([-value for value in self.value])

  @property
  def flat_values(self):
    for value in self.value:
      if isinstance(value, d):
        yield from value.fill_placeholders.flat_values
      else:
        yield value

    return None

  @property
  def width(self):
    x = 0.0
    widths = set[float]()
    for value in self.flat_values:
      widths.add(x)
      x = value.abs_x(x)
    widths.add(x)

    return max(widths) - min(widths)

  @property
  def height(self):
    y = 0.0
    heights = set[float]()
    for value in self.flat_values:
      heights.add(y)
      y = value.abs_y(y)
    heights.add(y)

    return max(heights) - min(heights)

  @property
  def rel_x(self):
    return reduce(lambda x, value: value.abs_x(x), self.flat_values, 0.0)

  @property
  def rel_y(self):
    return reduce(lambda y, value: value.abs_y(y), self.flat_values, 0.0)

  @property
  def fill_placeholders(self):
    width = self.width
    height = self.height
    return d([
        value.fill_placeholders
        if isinstance(value, d) else
        value.placeholder(width, height)
        for value in self.value
    ])

  def placeholder(self, width: float, height: float) -> DrawSegment:
    return d([
        value.placeholder(width, height)
        for value in self.value
    ])

  class m(DrawSegment):
    def __init__(self, x: float, y: float):
      self.x = x
      self.y = y

    def __format__(self, format_spec):
      return f'm {self.x:{format_spec}} {self.y:{format_spec}}'

    def __neg__(self):
      return d.m(-self.x, -self.y)

    @property
    def rel_x(self):
      return self.x

    @property
    def rel_y(self):
      return self.y

  class v(DrawSegment):
    def __init__(self, value: float):
      self.value = value

    def __add__(self, other: 'd.v'):
      return d.v(self.value + other.value)

    def __sub__(self, other: 'd.v'):
      return d.v(self.value - other.value)

    def __neg__(self):
      return d.v(-self.value)

    def __format__(self, format_spec):
      return f'v {self.value:{format_spec}}'

    @property
    def rel_y(self):
      return self.value

  class h(DrawSegment):
    def __init__(self, value: float):
      self.value = value

    def __add__(self, other: 'd.h'):
      return d.h(self.value + other.value)

    def __sub__(self, other: 'd.h'):
      return d.h(self.value - other.value)

    def __neg__(self):
      return d.h(-self.value)

    def __format__(self, format_spec):
      return f'h {self.value:{format_spec}}'

    @property
    def rel_x(self):
      return self.value

  class l(DrawSegment):
    def __init__(self, x: float, y: float):
      self.x = x
      self.y = y

    def __neg__(self):
      return d.l(-self.x, -self.y)

    def __format__(self, format_spec):
      return f'l {self.x:{format_spec}} {self.y:{format_spec}}'

    @property
    def rel_x(self):
      return self.x

    @property
    def rel_y(self):
      return self.y

  class c(DrawSegment):
    def __init__(self, dx1: float, dy1: float, dx2: float, dy2: float, dx: float, dy: float):
      self.dx1 = dx1
      self.dx2 = dx2
      self.dx = dx
      self.dy1 = dy1
      self.dy2 = dy2
      self.dy = dy

    def __neg__(self):
      return d.c(-self.dx1, -self.dy1, -self.dx2, -self.dy2, -self.dx, -self.dy)

    def __format__(self, format_spec):
      return f'c {self.dx1:{format_spec}} {self.dy1:{format_spec}} {self.dx2:{format_spec}} {self.dy2:{format_spec}} {self.dx:{format_spec}} {self.dy:{format_spec}}'

    @property
    def rel_x(self):
      return self.dx

    @property
    def rel_y(self):
      return self.dy

  class a(DrawSegment):
    def __init__(self, rx: float, ry: float, x_axis_rotation: float, large_arc_flag: bool, sweep_flag: bool, dx: float, dy: float):
      self.rx = rx
      self.ry = ry
      self.x_axis_rotation = x_axis_rotation
      self.large_arc_flag = large_arc_flag
      self.sweep_flag = sweep_flag
      self.dx = dx
      self.dy = dy

    def __neg__(self):
      return d.a(self.rx, self.ry, self.x_axis_rotation, self.large_arc_flag, self.sweep_flag, -self.dx, -self.dy)

    def __format__(self, format_spec):
      return f'a {self.rx:{format_spec}} {self.ry:{format_spec}} {self.x_axis_rotation} {1 if self.large_arc_flag else 0} {1 if self.sweep_flag else 0} {self.dx:{format_spec}} {self.dy:{format_spec}}'

    @property
    def rel_x(self):
      return self.dx

    @property
    def rel_y(self):
      return self.dy

  class z(DrawSegment):
    def __neg__(self):
      return self

    def __format__(self, format_spec):
      return 'z'


class placeholder(DrawSegment):
  def __init__(self, remaining: Callable[[float, float], DrawSegment]):
    self._remaining = remaining

  def __neg__(self):
    return placeholder(lambda width, height: -self.placeholder(width, height))

  def placeholder(self, width: float, height: float) -> DrawSegment:
    return self._remaining(width, height)


paint = none | color | Literal['context-fill'] | Literal['context-stroke']


@dataclass
class PresentationAttributes(Attributes):
  alignment_baseline: auto | Literal['baseline'] | Literal['before-edge'] | Literal['text-before-edge'] | Literal['middle'] | Literal['central'] | Literal[
      'after-edge'] | Literal['text-after-edge'] | Literal['ideographic'] | Literal['alphabetic'] | Literal['hanging'] | Literal['mathematical'] | inherit | None = None
  baseline_shift: auto | Literal['baseline'] | Literal['super'] | Literal['sub'] | length_percentage | inherit | None = None
  # clip: auto | <shape> | inherit | None = None
  # clip_path: none | <FuncIRI> | inherit | None = None
  clip_rule: Literal['nonzero'] | Literal['evenodd'] | inherit | None = None
  # color: color | inherit | None = None
  # color_interpolation: auto | sRGB | linearRGB | inherit | None = None
  # color_interpolation_filters: auto | sRGB | linearRGB | inherit | None = None
  # color_profile: auto | sRGB | linearRGB | <name> | <IRI> | inherit | None = None
  color_rendering: auto | Literal['optimizeSpeed'] | Literal['optimizeQuality'] | inherit | None = None
  # cursor: <FuncIRI>|<keywords>|inherit | None = None
  d: 'd | None' = None
  direction: Literal['ltr'] | Literal['rtl'] | inherit | None = None
  display: str | None = None
  dominant_baseline: Literal['auto'] | Literal['text-bottom'] | Literal['alphabetic'] | Literal['ideographic'] | Literal[
      'middle'] | Literal['central'] | Literal['mathematical'] | Literal['hanging'] | Literal['text-top'] | None = None
  enable_background: Literal['accumulate'] | Literal['new'] | inherit | None = None
  fill: paint | None = None
  fill_opacity: float | percentage | None = None
  fill_rule: Literal['nonzero'] | Literal['evenodd'] | inherit | None = None
  # filter: <FuncIRI> | none | inherit | None = None
  flood_color: color | None = None
  flood_opacity: float | percentage | None = None
  stroke: paint | None = None
  # stroke_dasharray: none | <dasharray> | None = None
  stroke_dashoffset: length_percentage | None = None
  stroke_linecap: Literal['butt'] | Literal['round'] | Literal['square'] | None = None
  stroke_linejoin: Literal['arcs'] | Literal['bevel'] | Literal['miter'] | Literal['miter-clip'] | Literal['round'] | None = None
  stroke_miterlimit: float | None = None
  stroke_opacity: float | percentage | None = None
  stroke_width: length_percentage | None = None
  transform: 'transform | Sequence[transform] | None' = None
