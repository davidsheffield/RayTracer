# Test src/ray_tracer/materials.py

import pytest

import ray_tracer


class TestAir:
    def test_name(self):
        assert ray_tracer.materials.air.name == 'Air'


    @pytest.mark.parametrize('wavelength',
                             [ray_tracer.Wavelength('2325.4', 2325.4),
                              ray_tracer.Wavelength('1970.1', 1970.1),
                              ray_tracer.Wavelength('1529.6', 1529.6),
                              ray_tracer.Wavelength('1060.0', 1060.0),
                              ray_tracer.Fraunhofer_line['t'],
                              ray_tracer.Fraunhofer_line['s'],
                              ray_tracer.Fraunhofer_line['r'],
                              ray_tracer.Fraunhofer_line['C'],
                              ray_tracer.Fraunhofer_line['Cprime'],
                              ray_tracer.Wavelength('632.8', 632.8),
                              ray_tracer.Fraunhofer_line['D'],
                              ray_tracer.Fraunhofer_line['d'],
                              ray_tracer.Fraunhofer_line['e'],
                              ray_tracer.Fraunhofer_line['F'],
                              ray_tracer.Fraunhofer_line['Fprime'],
                              ray_tracer.Fraunhofer_line['g'],
                              ray_tracer.Fraunhofer_line['h'],
                              ray_tracer.Fraunhofer_line['i'],
                              ray_tracer.Wavelength('334.1', 334.1),
                              ray_tracer.Wavelength('312.6', 312.6)])
    def test_index(self, wavelength):
        assert ray_tracer.materials.air.index[wavelength] == 1


class TestNBK7:
    def test_name(self):
        assert ray_tracer.materials.nbk7.name == 'SCHOTT N-BK 7 517642.251'


    @pytest.mark.parametrize(
        'wavelength,expected',
        [(ray_tracer.Wavelength('2325.4', 2325.4), 1.48921),
         (ray_tracer.Wavelength('1970.1', 1970.1), 1.49495),
         (ray_tracer.Wavelength('1529.6', 1529.6), 1.50091),
         (ray_tracer.Wavelength('1060.0', 1060.0), 1.50669),
         (ray_tracer.Fraunhofer_line['t'], 1.50731),
         (ray_tracer.Fraunhofer_line['s'], 1.50980),
         (ray_tracer.Fraunhofer_line['r'], 1.51289),
         (ray_tracer.Fraunhofer_line['C'], 1.51432),
         (ray_tracer.Fraunhofer_line['Cprime'], 1.51472),
         (ray_tracer.Wavelength('632.8', 632.8), 1.51509),
         (ray_tracer.Fraunhofer_line['D'], 1.51673),
         (ray_tracer.Fraunhofer_line['d'], 1.51680),
         (ray_tracer.Fraunhofer_line['e'], 1.51872),
         (ray_tracer.Fraunhofer_line['F'], 1.52238),
         (ray_tracer.Fraunhofer_line['Fprime'], 1.52283),
         (ray_tracer.Fraunhofer_line['g'], 1.52668),
         (ray_tracer.Fraunhofer_line['h'], 1.53024),
         (ray_tracer.Fraunhofer_line['i'], 1.53627),
         (ray_tracer.Wavelength('334.1', 334.1), 1.54272),
         (ray_tracer.Wavelength('312.6', 312.6), 1.54862)])
    def test_nbk7(self, wavelength, expected):
        assert ray_tracer.materials.nbk7.index[wavelength] == expected
