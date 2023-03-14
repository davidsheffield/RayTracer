# Test src/ray_tracer/optical_surface

import pytest

import ray_tracer


@pytest.fixture(scope='module')
def front_material():
    return ray_tracer.OpticalMaterial('Front',
                                      {ray_tracer.Fraunhofer_line['g']: 1.0,
                                       ray_tracer.Fraunhofer_line['F']: 1.0,
                                       ray_tracer.Fraunhofer_line['d']: 1.0})


@pytest.fixture(scope='module')
def back_material():
    return ray_tracer.OpticalMaterial('Back',
                                      {ray_tracer.Fraunhofer_line['F']: 1.5,
                                       ray_tracer.Fraunhofer_line['d']: 1.8,
                                       ray_tracer.Fraunhofer_line['C']: 1.6})


@pytest.fixture
def surface(front_material, back_material):
    """
    Set up OpticalSurface to test
    """

    return ray_tracer.OpticalSurface(0, 2, 12, front_material, back_material)


class TestVertex:
    def test_init(self, surface):
        assert surface.vertex == 0


    def test_setter(self, surface):
        surface.vertex = 1.0
        assert surface.vertex == 1


class TestRadiusCurvature:
    def test_radius_init(self, surface):
        assert surface.radius == 2
        assert surface.curvature == 0.5


    def test_radius_setter(self, surface):
        surface.radius = 10
        assert surface.radius == 10
        assert surface.curvature == 0.1
        assert surface.power[ray_tracer.Fraunhofer_line['F']] == 0.05
        assert surface.power[ray_tracer.Fraunhofer_line['d']] == pytest.approx(0.08)


    def test_curvature_setter(self, surface):
        surface.curvature = 0.2
        assert surface.radius == 5
        assert surface.curvature == 0.2
        assert surface.power[ray_tracer.Fraunhofer_line['F']] == 0.1
        assert surface.power[ray_tracer.Fraunhofer_line['d']] == pytest.approx(0.16)


class TestApertureHalfAperture:
    def test_init(self, surface):
        assert surface.aperture == 12
        assert surface.half_aperture == 6


    def test_aperture_setter(self, surface):
        surface.aperture = 10
        assert surface.aperture == 10
        assert surface.half_aperture == 5


    def test_half_aperture_setter(self, surface):
        surface.half_aperture = 4
        assert surface.aperture == 8
        assert surface.half_aperture == 4


class TestMaterials:
    def test_init(self, surface, front_material, back_material):
        assert surface.front_material is front_material
        assert surface.back_material is back_material


    def test_init_front_not_OpticalMaterial(self):
        with pytest.raises(TypeError):
            ray_tracer.OpticalSurface(0, 2, 12, 1, ray_tracer.materials.air)


    def test_init_back_not_OpticalMaterial(self):
        with pytest.raises(TypeError):
            ray_tracer.OpticalSurface(0, 2, 12, ray_tracer.materials.air, 1)


    def test_front_material_setter(self, surface, back_material):
        surface.front_material = ray_tracer.materials.nbk7
        assert surface.front_material is ray_tracer.materials.nbk7
        assert surface.back_material is back_material
        assert surface.power[ray_tracer.Fraunhofer_line['F']] == pytest.approx(-0.011190000000000033)
        assert surface.power[ray_tracer.Fraunhofer_line['d']] == pytest.approx(0.14160000000000006)
        assert surface.power[ray_tracer.Fraunhofer_line['C']] == pytest.approx(0.04283999999999999)


    def test_front_material_setter_not_OpticalMaterial(self, surface):
        with pytest.raises(TypeError):
            surface.front_material = 1


    def test_back_material_setter(self, surface, front_material):
        surface.back_material = ray_tracer.materials.nbk7
        assert surface.front_material is front_material
        assert surface.back_material is ray_tracer.materials.nbk7
        assert surface.power[ray_tracer.Fraunhofer_line['g']] == pytest.approx(0.26334)
        assert surface.power[ray_tracer.Fraunhofer_line['F']] == pytest.approx(0.26119000000000003)
        assert surface.power[ray_tracer.Fraunhofer_line['d']] == pytest.approx(0.25839999999999996)


    def test_back_material_setter_not_OpticalMaterial(self, surface):
        with pytest.raises(TypeError):
            surface.back_material = 1


class TestPower:
    def test_getter(self, surface):
        assert len(surface.power) == 2
        assert surface.power[ray_tracer.Fraunhofer_line['F']] == 0.25
        assert surface.power[ray_tracer.Fraunhofer_line['d']] == 0.4


    def test_power_setter(self, surface):
        with pytest.raises(AttributeError):
            surface.power = 2
