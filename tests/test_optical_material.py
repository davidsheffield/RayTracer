# Test src/ray_tracer/optical_material.py

import pytest

import ray_tracer


class TestName:
    def test_name(self):
        material = ray_tracer.OpticalMaterial('Air')
        assert material.name == 'Air'
        assert material.index == {}


    def test_name_not_str(self):
        with pytest.raises(TypeError):
            material = ray_tracer.OpticalMaterial(1)


class TestIndex:
    def test_index(self):
        index1 = ray_tracer.IndexOfRefraction('d', 1.5)
        index2 = ray_tracer.IndexOfRefraction('F', 1.6)
        material = ray_tracer.OpticalMaterial('Glass', [index1, index2])
        assert material.name == 'Glass'
        assert material.index['d'] is index1
        assert material.index['F'] is index2


    def test_not_IndexOfRefraction(self):
        with pytest.raises(TypeError):
            material = ray_tracer.OpticalMaterial(
                'Glass',
                [ray_tracer.IndexOfRefraction('d', 1.5),
                 1])


class TestAddIndex:
    def test_new_line(self):
        index = ray_tracer.IndexOfRefraction('d', 1.5)
        material = ray_tracer.OpticalMaterial('Glass')
        material.add_index(index)
        assert material.index['d'] is index


    def test_existing_line(self):
        material = ray_tracer.OpticalMaterial(
            'Glass',
            [ray_tracer.IndexOfRefraction('d', 1.5)])
        with pytest.raises(ValueError):
            material.add_index(ray_tracer.IndexOfRefraction('d', 1.6))


    def test_not_IndexOfRefraction(self):
        material = ray_tracer.OpticalMaterial('Glass')
        with pytest.raises(TypeError):
            material.add_index(1.6)


class TestUpdateIndex:
    def test_update_index(self):
        material = ray_tracer.OpticalMaterial(
            'Glass',
            [ray_tracer.IndexOfRefraction('d', 1.5)])
        material.update_index('d', 1.6)
        assert material.index['d'] == ray_tracer.IndexOfRefraction('d', 1.6)


    def test_no_existing_line(self):
        material = ray_tracer.OpticalMaterial(
            'Glass',
            [ray_tracer.IndexOfRefraction('d', 1.5)])
        with pytest.raises(KeyError):
            material.update_index('F', 1.6)
