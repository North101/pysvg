from .base import Type


class percentage(Type):
  def __init__(self, value: float):
    self.value = value

  def __round__(self, ndigits=0):
    return percentage(round(self.value, ndigits))

  def __format__(self, format_spec):
    return f'{self.value:{format_spec}}%'
