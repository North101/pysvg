from typing import Sequence

from ..attributes.base import format_attrs
from ..attributes.core import Attributes


class Element[Attrs: Attributes]:
  element: str

  def __init__(self, attrs: Attrs | None = None, children: Sequence['Element | str'] | str | None = None):
    self.attrs = attrs or Attributes()
    self.children = children or []

  def __iter__(self):
    yield from self.children

  def __format__(self, format_spec):
    element = self.element
    element_attrs = ' '.join((
        element,
        format_attrs(self.attrs, format_spec),
    ))
    children = f'\n{'\n'.join((
        f'\t{subchild}'
        for child in self.children
        for subchild in (str(child) if isinstance(child, str) else format(child, format_spec)).split('\n')
    ))}\n' if self.children and type(self.children) is not str else self.children
    if not children:
      return f'<{element_attrs}/>'

    return f'<{element_attrs}>{children}</{element}>'

  def __str__(self):
    return format(self)
