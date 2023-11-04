# Test src/ray_tracer/paraxial_ray

import pytest

import ray_tracer


def test_init():
    ray = ray_tracer.ParaxialRay(ray_tracer.Fraunhofer_line['d'], 0, 1, 0.5)
    assert ray.wavelength == ray_tracer.Fraunhofer_line['d']
    assert ray.z == [0]
    assert ray.y == [1]
    assert ray.u == [0.5]
    assert ray.optical_path_length == [0]


@pytest.fixture(scope='module')
def air():
    return ray_tracer.OpticalMaterial('Air',
                                      {ray_tracer.Fraunhofer_line['d']: 1.0})


@pytest.fixture(scope='module')
def glass():
    return ray_tracer.OpticalMaterial('Glass',
                                      {ray_tracer.Fraunhofer_line['d']: 1.5})


def test_propagate(air, glass):
    ray = ray_tracer.ParaxialRay(ray_tracer.Fraunhofer_line['d'], 0, 1, 0)
    surface1 = ray_tracer.OpticalSurface(10, 10, 4, air, glass)
    surface2 = ray_tracer.OpticalSurface(15, -10, 4, glass, air)
    system = ray_tracer.OpticalSystem([surface1, surface2])
    ray.propagate(system)
    assert ray.z == [0, 10, 15]
    assert ray.y == [1, 1, 0.8333333333333334]
    assert ray.u == [0, -0.03333333333333333, -0.1]
    assert ray.optical_path_length == [0, 10, 3.335184671067474]
