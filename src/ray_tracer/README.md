Source code
===========

[wavelength.py](wavelength.py): Defines the `Wavelength` class with the wavelength in nanometers and the name of the wavelength. It also defines`Fraunhofer_line` to reference the wavelengths of Fraunhofer lines by name.

[optical_material.py](optical_material.py): Defines the `OpticalMaterial` class, which represents a material through which light travels, such as glass or air. It contains the indices of refraction for that material.

[materials.py](materials.py): Instantiate `OpticalMeterial` objects for common materials, like air and N-BK7.

[optical_surface.py](optical_surface.py): Defines the `OpticalSurface` class, which represents a spherical surface between two materials. The class includes the vertex position, radius of curvature, aperture size, and materials on both sides of the surface. It calculates the power of the surface based on the curvature and materials. It also generates the coordinates to be able to draw a cross-sectional view of the surface.

[optical_system.py](optical_system.py): Defines the `OpticalSystem` class, which represents an optical system containing multiple `OpticalSurface` objects. It can draw the optical system.

[paraxial_ray.py](paraxial_ray.py): Defines the `ParaxialRay` class, which traces a ray of light using the paraxial approximation—the ray is sufficiently close to the optical axis that the angles are small. It includes attributes for the wavelength, coordinates, angles, and optical path length of the ray. It can also draw the ray.
