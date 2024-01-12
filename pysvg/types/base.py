class Type:
  def __init__(self, value):
    self.value = value

  def __format__(self, format_spec):
    return str(self.value)

  def __str__(self):
    return format(self)
