from dataclasses import dataclass, field
from typing import Optional


Fraunhofer_line = {'i': 365.01,
                   'h': 404.66,
                   'g': 435.84,
	           'Fprime': 479.99,
                   'F': 486.13,
                   'e': 546.07,
                   'd': 587.56,
                   'D': 589.3,
                   'Cprime': 643.85,
                   'C': 656.27,
                   'r': 706.52,
                   'Aprime': 768.2,
                   's': 852.11,
                   't': 1013.98}


@dataclass(order=True)
class IndexOfRefraction:
    """
    Class for the index of refraction at a specific wavelength.

    Attributes
    ----------
    line : str
        Fraunhofer line or wavelength in nanometers.
    index : float
        Index of refraction.
    wavelength : float
        Wavelength of the line in nanometers.
    """

    line : str = field(compare=False)
    _index : float
    wavelength : Optional[float] = field(default=None, compare=False)

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = float(value)

    def __post_init__(self):
        """
        If the line is defined, provide the wavelength.
        """

        if self.wavelength is None:
            try:
                self.wavelength = Fraunhofer_line[self.line]
            except KeyError:
                pass
