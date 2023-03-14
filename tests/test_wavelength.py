# Test src/ray_tracer/wavelength.py

import dataclasses
import typing

import pytest

import ray_tracer


class TestInit:
    def test_init(self):
        line = ray_tracer.Wavelength('500', 500.0)
        assert line.line == '500'
        assert line.wavelength == 500.0


    def test_int(self):
        line = ray_tracer.Wavelength('500', 500)
        assert isinstance(line.wavelength, float)
        assert line.wavelength == 500.0


    def test_nonnumeric(self):
        with pytest.raises(ValueError):
            line = ray_tracer.Wavelength('500', 'a')


class TestImmutable:
    @pytest.fixture
    def line(self):
        return ray_tracer.Wavelength('500', 500.0)


    def test_line(self, line):
        with pytest.raises(dataclasses.FrozenInstanceError):
            line.line = 'd'


    def test_wavelength(self, line):
        with pytest.raises(dataclasses.FrozenInstanceError):
            line.wavelength = 400.0


class TestComparison:
    def test_eq(self):
        line1 = ray_tracer.Wavelength('A', 500.0)
        line2 = ray_tracer.Wavelength('B', 500.0)
        assert line1 == line2


    def test_lt(self):
        line1 = ray_tracer.Wavelength('400', 400.0)
        line2 = ray_tracer.Wavelength('500', 500.0)
        assert line1 < line2


    def test_hashable(self):
        line = ray_tracer.Wavelength('500', 500.0)
        assert isinstance(line, typing.Hashable)


def test_Fraunhofer_line():
    lines = [['i', 365.01],
             ['h', 404.66],
             ['g', 435.84],
	     ['Fprime', 479.99],
             ['F', 486.13],
             ['e', 546.07],
             ['d', 587.56],
             ['D', 589.3],
             ['Cprime', 643.85],
             ['C', 656.27],
             ['r', 706.52],
             ['Aprime', 768.2],
             ['s', 852.11],
             ['t', 1013.98]]
    for row in lines:
        assert ray_tracer.Fraunhofer_line[row[0]].line == row[0]
        assert ray_tracer.Fraunhofer_line[row[0]].wavelength == row[1]
