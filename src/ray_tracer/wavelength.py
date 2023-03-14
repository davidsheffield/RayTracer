from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Wavelength:
    """
    Class for the wavelength of light. Once the values are set, the object
    is immutable.

    Attributes
    ----------
    line : str
        Fraunhofer line or wavelength in nanometers.
    wavelength : float
        Wavelength of the line in nanometers.
    """

    line : str = field(compare=False)
    wavelength : float

    def __post_init__(self):
        """
        Make sure the wavelength is a float. Need to use setattr because
        the attributes are frozen to make the objects hashable.
        """

        object.__setattr__(self, 'wavelength', float(self.wavelength))


Fraunhofer_line = {'i': Wavelength('i', 365.01),
                   'h': Wavelength('h', 404.66),
                   'g': Wavelength('g', 435.84),
	           'Fprime': Wavelength('Fprime', 479.99),
                   'F': Wavelength('F', 486.13),
                   'e': Wavelength('e', 546.07),
                   'd': Wavelength('d', 587.56),
                   'D': Wavelength('D', 589.3),
                   'Cprime': Wavelength('Cprime', 643.85),
                   'C': Wavelength('C', 656.27),
                   'r': Wavelength('r', 706.52),
                   'Aprime': Wavelength('Aprime', 768.2),
                   's': Wavelength('s', 852.11),
                   't': Wavelength('t', 1013.98)}
