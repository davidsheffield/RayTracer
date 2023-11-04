import matplotlib.pyplot as plt

import ray_tracer


def autocollimator():
    """
    Autocollimator
    """

    wavelength = ray_tracer.Fraunhofer_line['d']
    air = ray_tracer.materials.air
    nbk7 = ray_tracer.materials.nbk7

    system_forward = ray_tracer.OpticalSystem(
        [ray_tracer.OpticalSurface(
             vertex=94.77137790492614,
             radius=9e99,
             aperture=25.4,
             front_material=air,
             back_material=nbk7),
         ray_tracer.OpticalSurface(
             vertex=94.77137790492614 + 3,
             radius=-50,
             aperture=25.4,
             front_material=nbk7,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=150,
             radius=9e99,
             aperture=25.4,
             front_material=air,
             back_material=air)])
    
    fig, ax = system_forward.draw()

    ray_1a = ray_tracer.ParaxialRay(wavelength=wavelength,
                                    z0=0,
                                    y0=0,
                                    u0=0)
    ray_1a.propagate(system_forward)
    ray_1a.draw(ax)

    ray_1b = ray_tracer.ParaxialRay(wavelength=wavelength,
                                    z0=0,
                                    y0=0,
                                    u0=0.01)
    ray_1b.propagate(system_forward)
    ray_1b.draw(ax)

    ray_2a = ray_tracer.ParaxialRay(wavelength=wavelength,
                                    z0=0,
                                    y0=5,
                                    u0=0)
    ray_2a.propagate(system_forward)
    ray_2a.draw(ax, 'red')

    ray_2b = ray_tracer.ParaxialRay(wavelength=wavelength,
                                    z0=0,
                                    y0=5,
                                    u0=0.01)
    ray_2b.propagate(system_forward)
    ray_2b.draw(ax, 'red')

    ax.set_xlim(0, 150)
    ax.set_ylim(-12.8, 12.8)
    plt.show()

    system_backward = ray_tracer.OpticalSystem(
        [ray_tracer.OpticalSurface(
             vertex=150 - (94.77137790492614 + 3),
             radius=50,
             aperture=25.4,
             front_material=air,
             back_material=nbk7),
         ray_tracer.OpticalSurface(
             vertex=150 - 94.77137790492614,
             radius=9e99,
             aperture=25.4,
             front_material=nbk7,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=150,
             radius=9e99,
             aperture=25.4,
             front_material=air,
             back_material=air)])

    fig, ax = system_backward.draw()

    mirror_angle = 0.0

    ray_1a_back = ray_tracer.ParaxialRay(wavelength=wavelength,
                                         z0=0,
                                         y0=ray_1a.y[-1],
                                         u0=ray_1a.u[-1] + 2 * mirror_angle)
    ray_1a_back.propagate(system_backward)
    ray_1a_back.draw(ax)

    ray_1b_back = ray_tracer.ParaxialRay(wavelength=wavelength,
                                         z0=0,
                                         y0=ray_1b.y[-1],
                                         u0=ray_1b.u[-1] + 2 * mirror_angle)
    ray_1b_back.propagate(system_backward)
    ray_1b_back.draw(ax)

    ray_2a_back = ray_tracer.ParaxialRay(wavelength=wavelength,
                                         z0=0,
                                         y0=ray_2a.y[-1],
                                         u0=ray_2a.u[-1] + 2 * mirror_angle)
    ray_2a_back.propagate(system_backward)
    ray_2a_back.draw(ax, 'red')

    ray_2b_back = ray_tracer.ParaxialRay(wavelength=wavelength,
                                         z0=0,
                                         y0=ray_2b.y[-1],
                                         u0=ray_2b.u[-1] + 2 * mirror_angle)
    ray_2b_back.propagate(system_backward)
    ray_2b_back.draw(ax, 'red')

    print('y 1a', ray_1a_back.y[-1])
    print('y 1b', ray_1b_back.y[-1])
    print('y 2a', ray_2a_back.y[-1])
    print('y 2b', ray_2b_back.y[-1])
    print('Mirror angle', mirror_angle)

    ax.set_xlim(0, 150)
    ax.set_ylim(-12.8, 12.8)
    plt.show()


def get_back_focal_length():
    """
    Calculate the back focal length of a plano-convex lens
    with 50 mm radius of curvature and 3 mm thick.
    """

    wavelength = ray_tracer.Fraunhofer_line['d']
    air = ray_tracer.materials.air
    nbk7 = ray_tracer.materials.nbk7

    system = ray_tracer.OpticalSystem(
        [ray_tracer.OpticalSurface(
             vertex=10,
             radius=50,
             aperture=25.4,
             front_material=air,
             back_material=nbk7),
         ray_tracer.OpticalSurface(
             vertex=10 + 3,
             radius=9e99,
             aperture=25.4,
             front_material=nbk7,
             back_material=air),
         ray_tracer.OpticalSurface(
             vertex=150,
             radius=9e99,
             aperture=25.4,
             front_material=air,
             back_material=air)])
    
    fig, ax = system.draw()

    ray_marginal = ray_tracer.ParaxialRay(wavelength=wavelength,
                                          z0=0,
                                          y0=12.7,
                                          u0=0)
    ray_marginal.propagate(system)
    ray_marginal.draw(ax)

    print('Back Focal Length', -ray_marginal.y[-2] / ray_marginal.u[-2])

    ax.set_xlim(0, 150)
    ax.set_ylim(-13, 13)
    plt.show()


if __name__ == '__main__':
    autocollimator()
    # get_back_focal_length()
