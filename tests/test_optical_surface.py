# Test src/ray_tracer/optical_surface

import pytest

import ray_tracer


@pytest.fixture
def surface():
    """
    Set up OpticalSurface to test
    """

    return ray_tracer.OpticalSurface(
        0, 2, 12, ray_tracer.materials.air, ray_tracer.materials.air)


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


    def test_curvature_setter(self, surface):
        surface.curvature = 0.2
        assert surface.radius == 5
        assert surface.curvature == 0.2


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
    def test_init(self, surface):
        assert surface.front_material is ray_tracer.materials.air
        assert surface.back_material is ray_tracer.materials.air


    def test_init_front_not_OpticalMaterial(self):
        with pytest.raises(TypeError):
            ray_tracer.OpticalSurface(0, 2, 12, 1, ray_tracer.materials.air)


    def test_init_back_not_OpticalMaterial(self):
        with pytest.raises(TypeError):
            ray_tracer.OpticalSurface(0, 2, 12, ray_tracer.materials.air, 1)


    def test_front_material_setter(self, surface):
        surface.front_material = ray_tracer.materials.nbk7
        assert surface.front_material is ray_tracer.materials.nbk7
        assert surface.back_material is ray_tracer.materials.air


    def test_front_material_setter_not_OpticalMaterial(self, surface):
        with pytest.raises(TypeError):
            surface.front_material = 1


    def test_back_material_setter(self, surface):
        surface.back_material = ray_tracer.materials.nbk7
        assert surface.front_material is ray_tracer.materials.air
        assert surface.back_material is ray_tracer.materials.nbk7


    def test_back_material_setter_not_OpticalMaterial(self, surface):
        with pytest.raises(TypeError):
            surface.back_material = 1
