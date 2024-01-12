from ..attributes.base import format_attrs
from ..attributes.core import Attributes


class Element[Attrs: Attributes]:
  element: str

  def __init__(self, attrs: Attrs | None = None, children: list['Element | str'] | None = None):
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
    children = '\n'.join((
        f'\t{subchild}'
        for child in self.children
        for subchild in (str(child) if isinstance(child, str) else format(child, format_spec)).split('\n')
    ))
    if not children:
      return f'<{element_attrs}/>'

    return f'<{element_attrs}>\n{children}\n</{element}>'

  def __str__(self):
    return format(self)
