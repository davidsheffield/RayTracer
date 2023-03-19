# Test src/ray_tracer/optical_surface

import pytest

import numpy as np

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

    return ray_tracer.OpticalSurface(0, 2, 1, front_material, back_material)


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
        assert surface.aperture == 1.0
        assert surface.half_aperture == 0.5


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


    def test_setter(self, surface):
        with pytest.raises(AttributeError):
            surface.power = 2


class TestCrossSectionPoints:
    def test_init(self, surface):
        assert surface.cross_section_points == 51


    def test_setter(self, surface):
        surface.cross_section_points = 3
        assert surface.cross_section_points == 3


    def test_setter_minimum_value(self, surface):
        with pytest.raises(ValueError):
            surface.cross_section_points = 2


    def test_setter_minimum_value(self, surface):
        with pytest.raises(TypeError):
            surface.cross_section_points = 'a'


class TestCrossSection:
    def test_getter(self, surface):
        np.testing.assert_allclose(
            surface.cross_section,
            [[6.35083269e-02, 5.85537188e-02, 5.37974389e-02, 4.92399729e-02,
              4.48817865e-02, 4.07233248e-02, 3.67650127e-02, 3.30072546e-02,
              2.94504343e-02, 2.60949151e-02, 2.29410398e-02, 1.99891307e-02,
              1.72394892e-02, 1.46923963e-02, 1.23481122e-02, 1.02068763e-02,
              8.26890736e-03, 6.53440338e-03, 5.00354153e-03, 3.67647821e-03,
              2.55334897e-03, 1.63426855e-03, 9.19330844e-04, 4.08608878e-04,
              1.02154828e-04, 0.00000000e+00, 1.02154828e-04, 4.08608878e-04,
              9.19330844e-04, 1.63426855e-03, 2.55334897e-03, 3.67647821e-03,
              5.00354153e-03, 6.53440338e-03, 8.26890736e-03, 1.02068763e-02,
              1.23481122e-02, 1.46923963e-02, 1.72394892e-02, 1.99891307e-02,
              2.29410398e-02, 2.60949151e-02, 2.94504343e-02, 3.30072546e-02,
              3.67650127e-02, 4.07233248e-02, 4.48817865e-02, 4.92399729e-02,
              5.37974389e-02, 5.85537188e-02, 6.35083269e-02],
             [-5.00000000e-01, -4.80402266e-01, -4.60755457e-01,
              -4.41061579e-01, -4.21322645e-01, -4.01540671e-01,
              -3.81717677e-01, -3.61855689e-01, -3.41956736e-01,
              -3.22022850e-01, -3.02056068e-01, -2.82058429e-01,
              -2.62031977e-01, -2.41978757e-01, -2.21900818e-01,
              -2.01800210e-01, -1.81678988e-01, -1.61539206e-01,
              -1.41382922e-01, -1.21212195e-01, -1.01029086e-01,
              -8.08356566e-02, -6.06339691e-02, -4.04260875e-02,
              -2.02140762e-02, 0.00000000e+00, 2.02140762e-02, 4.04260875e-02,
              6.06339691e-02, 8.08356566e-02, 1.01029086e-01, 1.21212195e-01,
              1.41382922e-01, 1.61539206e-01, 1.81678988e-01, 2.01800210e-01,
              2.21900818e-01, 2.41978757e-01, 2.62031977e-01, 2.82058429e-01,
              3.02056068e-01, 3.22022850e-01, 3.41956736e-01, 3.61855689e-01,
              3.81717677e-01, 4.01540671e-01, 4.21322645e-01, 4.41061579e-01,
              4.60755457e-01, 4.80402266e-01, 5.00000000e-01]])


    def test_setter(self, surface):
        with pytest.raises(AttributeError):
            surface.cross_section = 2
