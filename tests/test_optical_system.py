# Test src/ray_tracer/opticalsystem

import pytest

import ray_tracer


@pytest.fixture(scope='module')
def material1():
    return ray_tracer.OpticalMaterial('Material1',
                                      {ray_tracer.Fraunhofer_line['g']: 1.0,
                                       ray_tracer.Fraunhofer_line['F']: 1.0,
                                       ray_tracer.Fraunhofer_line['d']: 1.0})


@pytest.fixture(scope='module')
def material2():
    return ray_tracer.OpticalMaterial('Material2',
                                      {ray_tracer.Fraunhofer_line['F']: 1.5,
                                       ray_tracer.Fraunhofer_line['d']: 1.8,
                                       ray_tracer.Fraunhofer_line['C']: 1.6})


@pytest.fixture
def surface1(material1, material2):
    """
    Set up OpticalSurface to test
    """

    return ray_tracer.OpticalSurface(0, 2, 1, material1, material2)

@pytest.fixture
def surface2(material1, material2):
    """
    Set up OpticalSurface to test
    """

    return ray_tracer.OpticalSurface(1, -2, 1, material2, material1)


class TestSurfaces:
    def test_in_order(self, surface1, surface2):
        system = ray_tracer.OpticalSystem([surface1, surface2])
        assert system.surfaces == [surface1, surface2]


    def test_out_of_order(self, surface1, surface2):
        system = ray_tracer.OpticalSystem([surface2, surface1])
        assert system.surfaces == [surface1, surface2]


    def test_inconsistent_materials(self, material1, material2):
        surface1 = ray_tracer.OpticalSurface(0, 2, 1, material1, material2)
        surface2 = ray_tracer.OpticalSurface(1, -2, 1, material1, material2)
        with pytest.raises(ValueError):
            system = ray_tracer.OpticalSystem([surface1, surface2])


class TestGetWavelengths:
    def test_get_wavelengths(self, surface1, surface2):
        system = ray_tracer.OpticalSystem([surface1, surface2])
        assert system.get_wavelengths() == [ray_tracer.Fraunhofer_line['F'],
                                            ray_tracer.Fraunhofer_line['d']]
