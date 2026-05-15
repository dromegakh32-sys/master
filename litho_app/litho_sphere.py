import trimesh

def sphere_lithophane(image, radius, shell_thickness):
    outer = trimesh.creation.icosphere(subdivisions=4, radius=radius)
    inner = trimesh.creation.icosphere(
        subdivisions=4, radius=radius - shell_thickness
    )
    return outer.difference(inner)
