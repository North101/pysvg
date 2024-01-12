from .base import Type


class transform(Type):
  pass


class transforms(Type):
  class translate(transform):
    def __init__(self, x: float, y: float | None = None):
      self.x = x
      self.y = y

    def __round__(self, ndigits=0):
      return transforms.translate(
          x=round(self.x, ndigits),
          y=round(self.y, ndigits) if self.y is not None else None,
      )

    def __format__(self, format_spec):
      if self.y is None:
        return f'translate({self.x:{format_spec}})'

      return f'translate({self.x:{format_spec}} {self.y:{format_spec}})'

  class scale(transform):
    def __init__(self, value: float):
      self.value = value

    def __round__(self, ndigits=0):
      return transforms.scale(round(self.value, ndigits))

    def __format__(self, format_spec):
      return f'scale({self.value:{format_spec}})'
