# Test src/ray_tracer/index_of_refraction.py

import pytest

import ray_tracer


def test_Fraunhofer_line():
    assert ray_tracer.Fraunhofer_line == {'i': 365.01,
                                          'h': 404.66,
                                          'g': 435.84,
	                                  'Fprime': 479.99,
                                          'F': 486.13,
                                          'e': 546.07,
                                          'd': 587.56,
                                          'D': 589.3,
                                          'Cprime': 643.85,
                                          'C': 656.27,
                                          'r': 706.52,
                                          'Aprime': 768.2,
                                          's': 852.11,
                                          't': 1013.98}


class TestInit:
    def test_unnamed_line_no_wavelength(self):
        n500 = ray_tracer.IndexOfRefraction('500', 1.5)
        n550 = ray_tracer.IndexOfRefraction('550', 1.6)
        assert n500.line == '500'
        assert n500.index == 1.5
        assert n500.wavelength is None
        assert n550.line == '550'
        assert n550.index == 1.6
        assert n550.wavelength is None


    def test_unnamed_line_with_wavelength(self):
        n500 = ray_tracer.IndexOfRefraction('500', 1.5, 500)
        assert n500.line == '500'
        assert n500.index == 1.5
        assert n500.wavelength == 500


    def test_named_line_no_wavelength(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5)
        assert nd.line == 'd'
        assert nd.index == 1.5
        assert nd.wavelength == ray_tracer.Fraunhofer_line['d']


    def test_named_line_with_wavelength(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5, 588)
        assert nd.line == 'd'
        assert nd.index == 1.5
        assert nd.wavelength == 588


class TestUpdateIndex:
    def test_update_index(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5)
        nd.index = 1.6
        assert nd.index == 1.6


    def test_not_float(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5)
        with pytest.raises(ValueError):
            nd.index = 'a'


    def test_int(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5)
        nd.index = 1
        assert nd.index == 1.0


class TestComparison:
    def test_eq(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5)
        n500 = ray_tracer.IndexOfRefraction('500', 1.5, 500)
        assert nd == n500


    def test_lt(self):
        nd = ray_tracer.IndexOfRefraction('d', 1.5)
        n500 = ray_tracer.IndexOfRefraction('500', 1.6, 500)
        assert nd < n500
