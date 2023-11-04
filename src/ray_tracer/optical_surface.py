import numpy as np

import ray_tracer


class OpticalSurface:
    """
    OpticalSurface
    --------------

    Spherical surface between two materials.

    Attributes
    ----------
    vertex : float
        Position [mm] where the surface crosses the optical axis.
    radius : float
        Radius [mm] of curvature for the surface. radius = 1 / curvature
    curvature : float
        Curvature [1 / mm] of the surface. curvature = 1 / radius
    aperture : float
        Diameter [mm] of the aperture of the surface.
    half_aperture : float
        Radius [mm] of the aperture of the surface.
    front_material : ray_tracer.OpticalMaterial
        Material to the front of the surface.
    back_material : ray_tracer.OpticalMaterial
        Material to the back of the surface.
    power : float
        Power of the surface.
    cross_section_points : int
        The number of points in cross_section.
    cross_section : np.array
        The (z, y) position of the cross section of the optical surface over the
        entire aperture with cross_section_points number of points.
    """

    def __init__(self, vertex, radius, aperture, front_material, back_material):
        if not isinstance(front_material, ray_tracer.OpticalMaterial) \
           or not isinstance(back_material, ray_tracer.OpticalMaterial):
            raise TypeError('Front and back materials must be ray_tracer.OpticalMaterial')
        self._vertex = vertex
        self._radius = radius
        self._curvature = 1.0 / radius
        self._aperture = aperture
        self._half_aperture = aperture / 2.0
        self._front_material = front_material
        self._back_material = back_material
        self._power = {}
        self._cross_section_points = 51
        self._cross_section = None

        self.update_power()
        self.update_cross_section()


    @property
    def vertex(self):
        return self._vertex


    @vertex.setter
    def vertex(self, value):
        self._vertex = value


    @property
    def radius(self):
        return self._radius


    @radius.setter
    def radius(self, value):
        self._radius = value
        self._curvature = 1.0 / value
        self.update_power()


    @property
    def curvature(self):
        return self._curvature


    @curvature.setter
    def curvature(self, value):
        self._curvature = value
        self._radius = 1.0 / value
        self.update_power()


    @property
    def aperture(self):
        return self._aperture


    @aperture.setter
    def aperture(self, value):
        self._aperture = value
        self._half_aperture = value / 2.0


    @property
    def half_aperture(self):
        return self._half_aperture


    @half_aperture.setter
    def half_aperture(self, value):
        self._half_aperture = value
        self._aperture = value * 2.0


    @property
    def front_material(self):
        return self._front_material


    @front_material.setter
    def front_material(self, material):
        if not isinstance(material, ray_tracer.OpticalMaterial):
            raise TypeError('material must be ray_tracer.OpticalMaterial')
        self._front_material = material
        self.update_power()


    @property
    def back_material(self):
        return self._back_material


    @back_material.setter
    def back_material(self, material):
        if not isinstance(material, ray_tracer.OpticalMaterial):
            raise TypeError('material must be ray_tracer.OpticalMaterial')
        self._back_material = material
        self.update_power()


    @property
    def power(self):
        return self._power


    def update_power(self):
        """
        Update power
        """

        self._power = {}
        for wavelength in (self._front_material.index.keys()
                           & self._back_material.index.keys()):
            self._power[wavelength] = ((self._back_material.index[wavelength]
                                        - self._front_material.index[wavelength])
                                       * self._curvature)


    @property
    def cross_section_points(self):
        return self._cross_section_points


    @cross_section_points.setter
    def cross_section_points(self, value):
        if value < 3:
            raise ValueError('Must have at least three points for the cross section')
        self._cross_section_points = int(value)


    @property
    def cross_section(self):
        return self._cross_section


    def update_cross_section(self):
        """
        Update cross_section
        """

        theta_max = np.arcsin(self._half_aperture / self._radius)
        theta = np.linspace(-theta_max, theta_max, 51)
        self._cross_section = np.array(
            [self._vertex + self._radius * (1 - np.cos(theta)),
             self._radius * np.sin(theta)])


    def __lt__(self, surface):
        return self._vertex < surface.vertex
