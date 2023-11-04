"""
Test the calculations by comparing against golden samples.
"""

import matplotlib.pyplot as plt

import ray_tracer


def edmunds_101_pcx():
    """
    From https://www.edmundoptics.com/knowledge-center/application-notes/optics/geometrical-optics-101-paraxial-ray-tracing-calculations/

    Plano-convex lens #49-849 25.4mm Diameter x 50.8mm FL lens.
    Using index of refraction 1 for air and 1.517 for N-BK7.
    Object plane is 25 mm from the 5 mm thick lens.
    """

    wavelength = ray_tracer.Fraunhofer_line['d']
    air = ray_tracer.materials.air
    nbk7 = ray_tracer.materials.nbk7
    nbk7.index[wavelength] = 1.517

    system = ray_tracer.OpticalSystem(
        [ray_tracer.OpticalSurface(
             vertex=25,
             radius=26.25,
             aperture=25.4,
             front_material=air,
             back_material=nbk7),
         ray_tracer.OpticalSurface(
             vertex=30,
             radius=9e99,
             aperture=25.4,
             front_material=nbk7,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=47.48 + 30,
             radius=9e99,
             aperture=25.4,
             front_material=air,
             back_material=air)])

    fig, ax = system.draw()

    ray_marginal = ray_tracer.ParaxialRay(wavelength=wavelength,
                                          z0=0,
                                          y0=1,
                                          u0=0)
    ray_marginal.propagate(system)
    ray_marginal.draw(ax)

    print('C', system.surfaces[0].curvature, system.surfaces[1].curvature)
    print('t', system.surfaces[0].vertex, system.surfaces[1].vertex - system.surfaces[0].vertex, system.surfaces[2].vertex - system.surfaces[1].vertex)
    print('n', system.surfaces[0].front_material.index[wavelength], system.surfaces[1].front_material.index[wavelength], system.surfaces[2].front_material.index[wavelength])
    print('-Φ', -system.surfaces[0].power[wavelength], -system.surfaces[1].power[wavelength])
    print('t/n', system.surfaces[0].vertex / system.surfaces[0].front_material.index[wavelength], (system.surfaces[1].vertex - system.surfaces[0].vertex) / system.surfaces[1].front_material.index[wavelength], (system.surfaces[2].vertex - system.surfaces[1].vertex) / system.surfaces[2].front_material.index[wavelength])
    print('y', ray_marginal.y[0], ray_marginal.y[1], ray_marginal.y[2], ray_marginal.y[3])
    print('nu', ray_marginal.u[0] * system.surfaces[0].front_material.index[wavelength], ray_marginal.u[1] * system.surfaces[1].front_material.index[wavelength], ray_marginal.u[2] * system.surfaces[2].front_material.index[wavelength])

    ax.set_xlim(0, 80)
    ax.set_ylim(-2, 2)
    plt.show()


def edmunds_101_dcv_dcx():
    """
    From https://www.edmundoptics.com/knowledge-center/application-notes/optics/geometrical-optics-101-paraxial-ray-tracing-calculations/

    Double-concave, double-convex system with an aperature.
    Using index of refraction 1 for air and 1.517 for N-BK7
    Object is 5 mm from front surface
    Double-concave lens with curvatures of 0.01 / mm that is 5 mm thick
    An aperture is 25 mm away and 10 mm diameter
    A double-convex lens is 25 mm away with curvatures of 0.025 / mm that is 8 mm thick
    """

    wavelength = ray_tracer.Fraunhofer_line['d']
    air = ray_tracer.materials.air
    nbk7 = ray_tracer.materials.nbk7
    nbk7.index[wavelength] = 1.517

    system = ray_tracer.OpticalSystem(
        [ray_tracer.OpticalSurface(
             vertex=5,
             radius=-1/0.01,
             aperture=20,
             front_material=air,
             back_material=nbk7),
         ray_tracer.OpticalSurface(
             vertex=10,
             radius=1/0.01,
             aperture=20,
             front_material=nbk7,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=35,
             radius=9e99,
             aperture=10,
             front_material=air,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=60,
             radius=1/0.025,
             aperture=20,
             front_material=air,
             back_material=nbk7),
         ray_tracer.OpticalSurface(
             vertex=68,
             radius=-1/0.025,
             aperture=20,
             front_material=nbk7,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=250,
             radius=9e99,
             aperture=20,
             front_material=air,
             back_material=air)])

    fig, ax = system.draw()

    ray_marginal = ray_tracer.ParaxialRay(wavelength=wavelength,
                                          z0=0,
                                          y0=0,
                                          u0=0.14731)
    ray_marginal.propagate(system)
    ray_marginal.draw(ax)

    ray_chief = ray_tracer.ParaxialRay(wavelength=wavelength,
                                       z0=0,
                                       y0=5,
                                       u0=-0.186)
    ray_chief.propagate(system)
    ray_chief.draw(ax)

    print('C', system.surfaces[0].curvature, system.surfaces[1].curvature, system.surfaces[2].curvature, system.surfaces[3].curvature, system.surfaces[4].curvature)
    print('t', system.surfaces[0].vertex, system.surfaces[1].vertex - system.surfaces[0].vertex, system.surfaces[2].vertex - system.surfaces[1].vertex, system.surfaces[3].vertex - system.surfaces[2].vertex, system.surfaces[4].vertex - system.surfaces[3].vertex, system.surfaces[5].vertex - system.surfaces[4].vertex)
    print('n', system.surfaces[0].front_material.index[wavelength], system.surfaces[1].front_material.index[wavelength], system.surfaces[2].front_material.index[wavelength], system.surfaces[3].front_material.index[wavelength], system.surfaces[4].front_material.index[wavelength], system.surfaces[5].front_material.index[wavelength])
    print('-Φ', -system.surfaces[0].power[wavelength], -system.surfaces[1].power[wavelength], -system.surfaces[2].power[wavelength], -system.surfaces[3].power[wavelength], -system.surfaces[4].power[wavelength])
    print('t/n', system.surfaces[0].vertex / system.surfaces[0].front_material.index[wavelength], (system.surfaces[1].vertex - system.surfaces[0].vertex) / system.surfaces[1].front_material.index[wavelength], (system.surfaces[2].vertex - system.surfaces[1].vertex) / system.surfaces[2].front_material.index[wavelength], (system.surfaces[3].vertex - system.surfaces[2].vertex) / system.surfaces[3].front_material.index[wavelength], (system.surfaces[4].vertex - system.surfaces[3].vertex) / system.surfaces[4].front_material.index[wavelength], (system.surfaces[5].vertex - system.surfaces[4].vertex) / system.surfaces[5].front_material.index[wavelength])
    print('')
    print('y', ray_marginal.y[0], ray_marginal.y[1], ray_marginal.y[2], ray_marginal.y[3], ray_marginal.y[4], ray_marginal.y[5], ray_marginal.y[6])
    print('nu', ray_marginal.u[0] * system.surfaces[0].front_material.index[wavelength], ray_marginal.u[1] * system.surfaces[1].front_material.index[wavelength], ray_marginal.u[2] * system.surfaces[2].front_material.index[wavelength], ray_marginal.u[3] * system.surfaces[3].front_material.index[wavelength], ray_marginal.u[4] * system.surfaces[4].front_material.index[wavelength], ray_marginal.u[5] * system.surfaces[5].front_material.index[wavelength])
    print('')
    print('y', ray_chief.y[0], ray_chief.y[1], ray_chief.y[2], ray_chief.y[3], ray_chief.y[4], ray_chief.y[5], ray_chief.y[6])
    print('nu', ray_chief.u[0] * system.surfaces[0].front_material.index[wavelength], ray_chief.u[1] * system.surfaces[1].front_material.index[wavelength], ray_chief.u[2] * system.surfaces[2].front_material.index[wavelength], ray_chief.u[3] * system.surfaces[3].front_material.index[wavelength], ray_chief.u[4] * system.surfaces[4].front_material.index[wavelength], ray_chief.u[5] * system.surfaces[5].front_material.index[wavelength])

    ax.set_xlim(0, 250)
    ax.set_ylim(-10, 10)
    plt.show()


if __name__ == '__main__':
    # edmunds_101_pcx()
    edmunds_101_dcv_dcx()
