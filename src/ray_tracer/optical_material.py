from dataclasses import dataclass, field
from typing import Optional

import ray_tracer


@dataclass
class OpticalMaterial:
    """
    OpticalMaterial
    ---------------

    Material (glass or air) that light travels through.

    Attributes
    ----------
    name : string
        Name of material.
    index : dict[ray_tracer.Wavelength, float]
        Indices of refraction.
    """

    name : str
    index : Optional[dict[ray_tracer.Wavelength, float]] = field(default=None)

    def __post_init__(self):
        """
        Check that name is a string and initialize index.
        """

        if not isinstance(self.name, str):
            raise TypeError('name must be a string')

        if self.index is None:
            self.index = {}
        else:
            if not all(isinstance(l, ray_tracer.Wavelength) for l in self.index.keys()):
                raise TypeError('index must be a dict with keys of type ray_tracer.Wavelength')
            try:
                self.index = {l: float(n) for (l, n) in self.index.items()}
            except ValueError:
                raise TypeError('index must be a dict with float values')


    def add_index(self, wavelength, index):
        """
        Add an index of refraction to the list of indices of refractions
        of the material.

        Parameters
        ----------
        wavelength : ray_tracer.Wavelength
            Wavelength of light.
        index : float
            Index of refraction.
        """

        if not isinstance(wavelength, ray_tracer.Wavelength):
            raise TypeError('wavelength must be of type ray_tracer.Wavelength')
        if wavelength in self.index.keys():
            raise ValueError('wavelength must be for a new line to add')
        self.index[wavelength] = float(index)


    def update_index(self, wavelength, index):
        """
        Update the index of refraction for a line.

        Parameters
        ----------
        wavelength : ray_tracer.Wavelength
            Wavelength of light.
        index : float
            Index of refraction.
        """

        if not isinstance(wavelength, ray_tracer.Wavelength):
            raise TypeError('wavelength must be of type ray_tracer.Wavelength')
        self.index[wavelength] = float(index)
