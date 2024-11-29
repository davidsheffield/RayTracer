"""
Instantiate `OpticalMeterial` objects for common materials.
"""


import ray_tracer


air = ray_tracer.OpticalMaterial(
    'Air',
    {ray_tracer.Wavelength('2325.4', 2325.4): 1,
     ray_tracer.Wavelength('1970.1', 1970.1): 1,
     ray_tracer.Wavelength('1529.6', 1529.6): 1,
     ray_tracer.Wavelength('1060.0', 1060.0): 1,
     ray_tracer.Fraunhofer_line['t']: 1,
     ray_tracer.Fraunhofer_line['s']: 1,
     ray_tracer.Fraunhofer_line['r']: 1,
     ray_tracer.Fraunhofer_line['C']: 1,
     ray_tracer.Fraunhofer_line['Cprime']: 1,
     ray_tracer.Wavelength('632.8', 632.8): 1,
     ray_tracer.Fraunhofer_line['D']: 1,
     ray_tracer.Fraunhofer_line['d']: 1,
     ray_tracer.Fraunhofer_line['e']: 1,
     ray_tracer.Fraunhofer_line['F']: 1,
     ray_tracer.Fraunhofer_line['Fprime']: 1,
     ray_tracer.Fraunhofer_line['g']: 1,
     ray_tracer.Fraunhofer_line['h']: 1,
     ray_tracer.Fraunhofer_line['i']: 1,
     ray_tracer.Wavelength('334.1', 334.1): 1,
     ray_tracer.Wavelength('312.6', 312.6): 1})


nbk7 = ray_tracer.OpticalMaterial(
    'SCHOTT N-BK 7 517642.251',
    {ray_tracer.Wavelength('2325.4', 2325.4): 1.48921,
     ray_tracer.Wavelength('1970.1', 1970.1): 1.49495,
     ray_tracer.Wavelength('1529.6', 1529.6): 1.50091,
     ray_tracer.Wavelength('1060.0', 1060.0): 1.50669,
     ray_tracer.Fraunhofer_line['t']: 1.50731,
     ray_tracer.Fraunhofer_line['s']: 1.50980,
     ray_tracer.Fraunhofer_line['r']: 1.51289,
     ray_tracer.Fraunhofer_line['C']: 1.51432,
     ray_tracer.Fraunhofer_line['Cprime']: 1.51472,
     ray_tracer.Wavelength('632.8', 632.8): 1.51509,
     ray_tracer.Fraunhofer_line['D']: 1.51673,
     ray_tracer.Fraunhofer_line['d']: 1.51680,
     ray_tracer.Fraunhofer_line['e']: 1.51872,
     ray_tracer.Fraunhofer_line['F']: 1.52238,
     ray_tracer.Fraunhofer_line['Fprime']: 1.52283,
     ray_tracer.Fraunhofer_line['g']: 1.52668,
     ray_tracer.Fraunhofer_line['h']: 1.53024,
     ray_tracer.Fraunhofer_line['i']: 1.53627,
     ray_tracer.Wavelength('334.1', 334.1): 1.54272,
     ray_tracer.Wavelength('312.6', 312.6): 1.54862})
