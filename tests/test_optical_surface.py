# Test src/ray_tracer/optical_surface

import ray_tracer


def test_vertex():
    surface = ray_tracer.OpticalSurface(0, 1, 12)
    assert surface.vertex == 0
    surface.vertex = 1.0
    assert surface.vertex == 1


def test_radius_curvature():
    surface = ray_tracer.OpticalSurface(0, 2, 12)
    assert surface.radius == 2
    assert surface.curvature == 0.5
    surface.radius = 10
    assert surface.radius == 10
    assert surface.curvature == 0.1
    surface.curvature = 0.2
    assert surface.radius == 5
    assert surface.curvature == 0.2


def test_aperture_half_aperture():
    surface = ray_tracer.OpticalSurface(0, 1, 12)
    assert surface.aperture == 12
    assert surface.half_aperture == 6
    surface.aperture = 10
    assert surface.aperture == 10
    assert surface.half_aperture == 5
    surface.half_aperture = 4
    assert surface.aperture == 8
    assert surface.half_aperture == 4
