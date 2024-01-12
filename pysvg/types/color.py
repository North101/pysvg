from .base import Type
from .named_color import named_color


class hex_color(Type):
  def __init__(self, value: str):
    self.value = value


class rgb(Type):
  def __init__(self, r: int, g: int, b: int):
    self.r = r
    self.g = g
    self.b = b

  def __format__(self, format_spec):
    return f'rgb({self.r:{format_spec}} {self.g:{format_spec}} {self.b:{format_spec}})'


class hsl(Type):
  def __init__(self, h: int, s: float, l: float):
    self.h = h
    self.s = s
    self.l = l

  def __format__(self, format_spec):
    return f'hsl({self.h:{format_spec}} {self.s:{format_spec}} {self.l:{format_spec}})'


class hwb(Type):
  def __init__(self, h: int, w: float, b: float):
    self.h = h
    self.w = w
    self.b = b

  def __format__(self, format_spec):
    return f'hwb({self.h:{format_spec}} {self.w:{format_spec}} {self.b:{format_spec}})'


class lab(Type):
  def __init__(self, l: float, a: int, b: float):
    self.l = l
    self.a = a
    self.b = b

  def __format__(self, format_spec):
    return f'lab({self.l:{format_spec}} {self.a:{format_spec}} {self.b:{format_spec}})'


class lch(Type):
  def __init__(self, l: float, c: int, h: float):
    self.l = l
    self.c = c
    self.h = h

  def __format__(self, format_spec):
    return f'lch({self.l:{format_spec}} {self.c:{format_spec}} {self.h:{format_spec}})'


class oklab(Type):
  def __init__(self, l: float, a: float, b: float):
    self.l = l
    self.a = a
    self.b = b

  def __format__(self, format_spec):
    return f'oklab({self.l:{format_spec}} {self.a:{format_spec}} {self.b:{format_spec}})'


class oklch(Type):
  def __init__(self, l: float, c: float, h: float):
    self.l = l
    self.c = c
    self.h = h

  def __format__(self, format_spec):
    return f'oklch({self.l:{format_spec}} {self.c:{format_spec}} {self.h:{format_spec}})'


class light_dark(Type):
  def __init__(self, light: named_color | rgb, dark: named_color | rgb):
    self.light = light
    self.dark = dark

  def __format__(self, format_spec):
    return f'light-dark({self.light:{format_spec}} {self.dark:{format_spec}})'


color = named_color | hex_color | rgb | hsl | hwb | lab | lch | oklab | oklch | light_dark
