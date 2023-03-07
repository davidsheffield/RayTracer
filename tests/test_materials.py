# Test src/ray_tracer/materials.py

import ray_tracer


def test_air():
    expected = [['2325.4', 2325.4],
                ['1970.1', 1970.1],
                ['1529.6', 1529.6],
                ['1060.0', 1060.0],
                ['t', 1014.0],
                ['s', 852.1],
                ['r', 706.5],
                ['C', 656.3],
                ['Cprime', 643.8],
                ['632.8', 632.8],
                ['D', 589.3],
                ['d', 587.6],
                ['e', 546.1],
                ['F', 486.1],
                ['Fprime', 480.0],
                ['g', 435.8],
                ['h', 404.7],
                ['i', 365.0],
                ['334.1', 334.1],
                ['312.6', 312.6]]
    for line in expected:
        assert ray_tracer.materials.air.index[line[0]].index == 1.0
        assert ray_tracer.materials.air.index[line[0]].wavelength == line[1]


def test_nbk7():
    expected = [['2325.4', 1.48921, 2325.4],
                ['1970.1', 1.49495, 1970.1],
                ['1529.6', 1.50091, 1529.6],
                ['1060.0', 1.50669, 1060.0],
                ['t', 1.50731, 1014.0],
                ['s', 1.50980, 852.1],
                ['r', 1.51289, 706.5],
                ['C', 1.51432, 656.3],
                ['Cprime', 1.51472, 643.8],
                ['632.8', 1.51509, 632.8],
                ['D', 1.51673, 589.3],
                ['d', 1.51680, 587.6],
                ['e', 1.51872, 546.1],
                ['F', 1.52238, 486.1],
                ['Fprime', 1.52283, 480.0],
                ['g', 1.52668, 435.8],
                ['h', 1.53024, 404.7],
                ['i', 1.53627, 365.0],
                ['334.1', 1.54272, 334.1],
                ['312.6', 1.54862, 312.6]]
    for line in expected:
        assert ray_tracer.materials.nbk7.index[line[0]].index == line[1]
        assert ray_tracer.materials.nbk7.index[line[0]].wavelength == line[2]
