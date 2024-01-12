from dataclasses import asdict, dataclass


def _dict_factory(x):
  return {
      k: v
      for (k, v) in x
      if v is not None
  }


def format_attrs(attrs: 'Attributes', format_spec: str, namespace: str | None = None):
  return ' '.join((
      format_attr(k, v, format_spec, namespace)
      for k, v in asdict(attrs, dict_factory=_dict_factory).items()
  ))


def format_attr(key: str, value, format_spec: str, namespace: str | None = None) -> str:
  if isinstance(value, Attributes):
    return format_attrs(value, key, format_spec)

  key = key.replace('_', '-')
  if namespace:
    return f'{namespace}:{key}="{format_attr_value(value, format_spec)}"'

  return f'{key}="{format_attr_value(value, format_spec)}"'


def format_attr_value(value, format_spec):
  if isinstance(value, list | tuple | set):
    return ' '.join((
        format_attr_value(v, format_spec)
        for v in value
    ))

  elif isinstance(value, str):
    return value

  return format(value, format_spec)


class Attribute():
  def __init__(self, value):
    self.value = value

  def __format__(self):
    return str(self.value)

  def __str__(self):
    return format(self)


@dataclass
class Attributes():
  def __or__(self, other):
    return self.__class__(**asdict(
        self,
        dict_factory=_dict_factory,
    ) | asdict(
        other,
        dict_factory=_dict_factory,
    ))
