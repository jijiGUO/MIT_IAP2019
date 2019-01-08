import compas

from compas.datastructures import Mesh
from compas.geometry import smooth_centroid

from compas.plotters import Plotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

fixed = [key for key in mesh.vertices() if mesh.vertex_degree(key) == 2]

points = []
for key in mesh.vertices():
    points.append({
        'pos':
        mesh.vertex_coordinates(key),
        'radius':
        0.1,
        'facecolor':
        '#ff0000' if mesh.vertex_degree(key) == 2 else '#ffffff'
    })

lines = []
for u, v in mesh.edges():
    lines.append({
        'start': mesh.vertex_coordinates(u),
        'end': mesh.vertex_coordinates(v),
        'width': 1.0
    })

plotter = Plotter(figsize=(10, 6))

pcoll = plotter.draw_points(points)
lcoll = plotter.draw_lines(lines)


def callback(k, args):
    plotter.update_pointcollection(pcoll, vertices, 0.1)

    segments = []
    for u, v in mesh.edges():
        a = vertices[u][0:2]
        b = vertices[v][0:2]
        segments.append([a, b])

    plotter.update_linecollection(lcoll, segments)
    plotter.update(pause=0.001)


vertices = [mesh.vertex_coordinates(key) for key in mesh.vertices()]
adjacency = [mesh.vertex_neighbors(key) for key in mesh.vertices()]

smooth_centroid(vertices, adjacency, fixed=fixed, kmax=100, callback=callback)

plotter.show()
