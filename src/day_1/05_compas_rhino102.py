import compas

from compas.datastructures import Mesh
from compas.geometry import smooth_centroid

from compas_rhino.artists import MeshArtist
from compas_rhino.conduits import LinesConduit

mesh = Mesh.from_obj(compas.get('faces.obj'))

fixed = [key for key in mesh.vertices() if mesh.vertex_degree(key) == 2]

lines = []
for u, v in mesh.edges():
    lines.append([mesh.vertex_coordinates(u), mesh.vertex_coordinates(v)])

conduit = LinesConduit(lines, refreshrate=1)


def callback(k, args):

    segments = []
    for u, v in mesh.edges():
        a = vertices[u][0:3]
        b = vertices[v][0:3]
        segments.append([a, b])

    conduit.lines = segments
    conduit.redraw(k)


vertices = [mesh.vertex_coordinates(key) for key in mesh.vertices()]
adjacency = [mesh.vertex_neighbors(key) for key in mesh.vertices()]

with conduit.enabled():
    smooth_centroid(
        vertices, adjacency, fixed=fixed, kmax=100, callback=callback)

for key, attr in mesh.vertices(True):
    attr['x'] = vertices[key][0]
    attr['y'] = vertices[key][1]
    attr['z'] = vertices[key][2]

artist = MeshArtist(mesh, layer='mesh-out')
artist.draw_faces(join_faces=True)
