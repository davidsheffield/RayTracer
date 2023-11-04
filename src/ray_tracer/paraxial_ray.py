import math

import ray_tracer


class ParaxialRay:
    """
    ParaxialRay
    -----------

    Ray of light whose ray trace is from the paraxial approximation.

    Attributes
    ----------
    wavelength : ray_tracer.Wavelength
        Wavelength of the ray.
    z : list(float)
        List of z coordinates along the axis of the optical system in millimeters.
    y : list(float)
        List of y coordinates transverse to the optical system in millimeters.
    u : list(float)
        List of angles of the direction of the ray relative to the optical axis in radians.
    optical_path_length : list(float)
        Optical path length of the ray.
    """

    def __init__(self, wavelength, z0, y0, u0):
        """
        Parameters
        ----------
        Wavelength : ray_tracer.Wavelength
            Wavelength of the ray.
        z0 : float
            Initial z coordinate along the axis of the optical system in millimeters.
        y0 : float
            Initial y coordinate transverse to the optical system in millimeters.
        u : float
            Initial angle of the direction of the ray relative to the optical axis in radians.
        """

        self.wavelength = wavelength
        self.z = [z0]
        self.y = [y0]
        self.u = [u0]
        self.optical_path_length = [0]


    def propagate(self, system):
        """
        Parameters
        ----------
        system : ray_tracer.OpticalSystem
            Optical system to trace the ray through.
        """

        for surface in system.surfaces:
            self.z.append(surface.vertex)
            self.y.append(self.y[-1] + self.u[-1] * (self.z[-1] - self.z[-2]))
            self.u.append((surface.front_material.index[self.wavelength]
                           * self.u[-1]
                           - self.y[-2]
                           * surface.power[self.wavelength])
                          / surface.back_material.index[self.wavelength])
            self.optical_path_length.append(
                math.sqrt((self.z[-1] - self.z[-2]) ** 2
                          + (self.y[-1] - self.y[-2]) ** 2)
                / surface.front_material.index[self.wavelength])


    def draw(self, ax):
        """
        Draw the ray.

        Parameters
        ----------
        ax : matplotlib.axes._axes.Axes
            Plot of optical system.
        """

        ax.plot(self.z,
                self.y,
                color='blue')
