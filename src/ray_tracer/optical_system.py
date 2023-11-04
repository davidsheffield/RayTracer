import itertools

import matplotlib.pyplot as plt

import ray_tracer


class OpticalSystem:
    """
    OpticalSystem
    -------------

    Optical system containing optical surfaces.

    Attributes
    ----------
    surfaces : list[ray_tracer.OpticalSurface]
        Collection of optical surfaces in the system.
    """

    def __init__(self, surfaces):
        self.surfaces = sorted(surfaces)
        for surface1, surface2 in itertools.pairwise(self.surfaces):
            if surface1.back_material != surface2.front_material:
                raise ValueError('Adjacent surfaces must share the same material.')


    def draw(self):
        """
        Draw the optical system.
        """
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        for surface in self.surfaces:
            ax.plot(surface.cross_section[0],
                    surface.cross_section[1],
                    color='black')
        ax.set_xlim([0, 50])
        ax.set_ylim([-6, 6])
        ax.xaxis.set_tick_params(labelbottom=False)
        ax.yaxis.set_tick_params(labelleft=False)
        ax.set_xticks([])
        ax.set_yticks([])
        return fig, ax


    def get_wavelengths(self):
        """
        Returns
        -------
        list[ray_tracer.Wavelength]
            A list of wavelengths that the materials in the systems have defined
            indices of refraction.
        """

        wavelengths_of_materials = [
            list(surface.__getattribute__(attribute).index.keys())
            for surface in self.surfaces
            for attribute in ['front_material', 'back_material']]
        return [wavelength for wavelength
                in set.intersection(*map(set, wavelengths_of_materials))]
