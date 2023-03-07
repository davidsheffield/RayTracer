import ray_tracer


air = ray_tracer.OpticalMaterial(
    'Air',
    [ray_tracer.IndexOfRefraction('2325.4', 1, 2325.4),
     ray_tracer.IndexOfRefraction('1970.1', 1, 1970.1),
     ray_tracer.IndexOfRefraction('1529.6', 1, 1529.6),
     ray_tracer.IndexOfRefraction('1060.0', 1, 1060.0),
     ray_tracer.IndexOfRefraction('t', 1, 1014.0),
     ray_tracer.IndexOfRefraction('s', 1, 852.1),
     ray_tracer.IndexOfRefraction('r', 1, 706.5),
     ray_tracer.IndexOfRefraction('C', 1, 656.3),
     ray_tracer.IndexOfRefraction('Cprime', 1, 643.8),
     ray_tracer.IndexOfRefraction('632.8', 1, 632.8),
     ray_tracer.IndexOfRefraction('D', 1, 589.3),
     ray_tracer.IndexOfRefraction('d', 1, 587.6),
     ray_tracer.IndexOfRefraction('e', 1, 546.1),
     ray_tracer.IndexOfRefraction('F', 1, 486.1),
     ray_tracer.IndexOfRefraction('Fprime', 1, 480.0),
     ray_tracer.IndexOfRefraction('g', 1, 435.8),
     ray_tracer.IndexOfRefraction('h', 1, 404.7),
     ray_tracer.IndexOfRefraction('i', 1, 365.0),
     ray_tracer.IndexOfRefraction('334.1', 1, 334.1),
     ray_tracer.IndexOfRefraction('312.6', 1, 312.6)])


nbk7 = ray_tracer.OpticalMaterial(
    'SCHOTT N-BK 7 517642.251',
    [ray_tracer.IndexOfRefraction('2325.4', 1.48921, 2325.4),
     ray_tracer.IndexOfRefraction('1970.1', 1.49495, 1970.1),
     ray_tracer.IndexOfRefraction('1529.6', 1.50091, 1529.6),
     ray_tracer.IndexOfRefraction('1060.0', 1.50669, 1060.0),
     ray_tracer.IndexOfRefraction('t', 1.50731, 1014.0),
     ray_tracer.IndexOfRefraction('s', 1.50980, 852.1),
     ray_tracer.IndexOfRefraction('r', 1.51289, 706.5),
     ray_tracer.IndexOfRefraction('C', 1.51432, 656.3),
     ray_tracer.IndexOfRefraction('Cprime', 1.51472, 643.8),
     ray_tracer.IndexOfRefraction('632.8', 1.51509, 632.8),
     ray_tracer.IndexOfRefraction('D', 1.51673, 589.3),
     ray_tracer.IndexOfRefraction('d', 1.51680, 587.6),
     ray_tracer.IndexOfRefraction('e', 1.51872, 546.1),
     ray_tracer.IndexOfRefraction('F', 1.52238, 486.1),
     ray_tracer.IndexOfRefraction('Fprime', 1.52283, 480.0),
     ray_tracer.IndexOfRefraction('g', 1.52668, 435.8),
     ray_tracer.IndexOfRefraction('h', 1.53024, 404.7),
     ray_tracer.IndexOfRefraction('i', 1.53627, 365.0),
     ray_tracer.IndexOfRefraction('334.1', 1.54272, 334.1),
     ray_tracer.IndexOfRefraction('312.6', 1.54862, 312.6)])
