# Test src/ray_tracer/optical_material.py

import pytest

import ray_tracer


class TestInit:
    def test_name(self):
        material = ray_tracer.OpticalMaterial('Air')
        assert material.name == 'Air'
        assert material.index == {}


    def test_name_not_str(self):
        with pytest.raises(TypeError):
            material = ray_tracer.OpticalMaterial(1)


    def test_index(self):
        material = ray_tracer.OpticalMaterial(
            'Glass',
            {ray_tracer.Fraunhofer_line['d']: 1.5,
             ray_tracer.Fraunhofer_line['F']: 1.6})
        assert material.name == 'Glass'
        assert material.index[ray_tracer.Fraunhofer_line['d']] == 1.5
        assert material.index[ray_tracer.Fraunhofer_line['F']] == 1.6


    def test_index_not_Wavelength(self):
        with pytest.raises(TypeError):
            material = ray_tracer.OpticalMaterial('Glass', {500.0: 1.5})


    def test_index_not_nomeric(self):
        with pytest.raises(TypeError):
            material = ray_tracer.OpticalMaterial(
                'Glass',
                {ray_tracer.Fraunhofer_line['d']: 'a'})


@pytest.fixture
def material():
    return ray_tracer.OpticalMaterial('Glass')


@pytest.fixture
def material_with_index():
    return ray_tracer.OpticalMaterial(
        'Glass',
        {ray_tracer.Fraunhofer_line['d']: 1.5})


class TestAddIndex:
    def test_new_line_no_indices(self, material):
        material.add_index(ray_tracer.Fraunhofer_line['d'], 1.5)
        assert material.index[ray_tracer.Fraunhofer_line['d']] == 1.5


    def test_new_line_existing_indices(self, material_with_index):
        material_with_index.add_index(ray_tracer.Fraunhofer_line['F'], 1.6)
        assert material_with_index.index[ray_tracer.Fraunhofer_line['d']] == 1.5
        assert material_with_index.index[ray_tracer.Fraunhofer_line['F']] == 1.6


    def test_existing_line(self, material_with_index):
        with pytest.raises(ValueError):
            material_with_index.add_index(ray_tracer.Fraunhofer_line['d'], 1.5)


    def test_not_Wavelength(self, material):
        with pytest.raises(TypeError):
            material.add_index(500, 1.5)


    def test_nonnumeric(self, material):
        with pytest.raises(ValueError):
            material.add_index(ray_tracer.Fraunhofer_line['d'], 'a')


    def test_int_index(self, material):
        material.add_index(ray_tracer.Fraunhofer_line['d'], 1)
        assert isinstance(material.index[ray_tracer.Fraunhofer_line['d']], float)
        assert material.index[ray_tracer.Fraunhofer_line['d']] == 1.0


class TestUpdateIndex:
    def test_no_existing_index(self, material):
        material.update_index(ray_tracer.Fraunhofer_line['F'], 1.6)
        assert material.index[ray_tracer.Fraunhofer_line['F']] == 1.6


    def test_with_existing_index(self, material_with_index):
        material_with_index.update_index(ray_tracer.Fraunhofer_line['F'], 1.6)
        assert material_with_index.index[ray_tracer.Fraunhofer_line['d']] == 1.5
        assert material_with_index.index[ray_tracer.Fraunhofer_line['F']] == 1.6


    def test_overwrite_existing_index(self, material_with_index):
        material_with_index.update_index(ray_tracer.Fraunhofer_line['d'], 1.6)
        assert material_with_index.index[ray_tracer.Fraunhofer_line['d']] == 1.6
        assert len(material_with_index.index) == 1


    def test_not_Wavelength(self, material):
        with pytest.raises(TypeError):
            material.update_index(500, 1.5)


    def test_nonnumeric(self, material):
        with pytest.raises(ValueError):
            material.update_index(ray_tracer.Fraunhofer_line['d'], 'a')
