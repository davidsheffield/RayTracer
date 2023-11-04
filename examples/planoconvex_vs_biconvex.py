import matplotlib.pyplot as plt

import ray_tracer


def biconvex():
    """
    Ray tracer of a biconvex lens.
    """

    system = ray_tracer.OpticalSystem(
        [ray_tracer.OpticalSurface(
            20, 10, 10, ray_tracer.materials.air, ray_tracer.materials.nbk7),
         ray_tracer.OpticalSurface(
             25, -10, 10, ray_tracer.materials.nbk7, ray_tracer.materials.air),
         ray_tracer.OpticalSurface(
             40, 9e99, 10, ray_tracer.materials.air, ray_tracer.materials.air)])
    fig, ax = system.draw()

    ray_axial = ray_tracer.ParaxialRay(ray_tracer.Fraunhofer_line['d'], 0, 0, 0)
    ray_axial.propagate(system)
    ray_axial.draw(ax)

    ray_paraxial = ray_tracer.ParaxialRay(ray_tracer.Fraunhofer_line['d'], 0, 1, 0)
    ray_paraxial.propagate(system)
    ray_paraxial.draw(ax)

    ray_marginal = ray_tracer.ParaxialRay(ray_tracer.Fraunhofer_line['d'], 0, system.surfaces[0].half_aperture, 0)
    ray_marginal.propagate(system)
    ray_marginal.draw(ax)

    plt.show()


if __name__ == '__main__':
    biconvex()
