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
    index : set[ray_tracer.IndexOfRefraction]
        Indices of refraction.
    """

    name : str
    index : Optional[dict[ray_tracer.IndexOfRefraction]] = field(default=None)

    def __post_init__(self):
        """
        Initialize index.
        """

        if not isinstance(self.name, str):
            raise TypeError('name must be a string')

        if self.index is None:
            self.index = {}
        else:
            if not all(isinstance(n, ray_tracer.IndexOfRefraction) for n in self.index):
                raise TypeError('index must be a list of type ray_tracer.IndexOfRefraction')
            self.index = {n.line: n for n in self.index}



    def add_index(self, index):
        """
        Add an index of refraction to the list of indices of refractions
        of the material.

        Parameters
        ----------
        index : ray_tracer.IndexOfRefraction
            Index of refraction.
        """

        if not isinstance(index, ray_tracer.IndexOfRefraction):
            raise TypeError('index must be of type ray_tracer.IndexOfRefraction')
        if index.line in self.index.keys():
            raise ValueError('index must be for a new line to add')
        self.index[index.line] = index


    def update_index(self, line, index):
        """
        Update the index of refraction for a line.

        Parameters
        ----------
        line : str
            Line to update index of refraction for.
        index : float
            Index of refraction.
        """

        self.index[line].index = index
