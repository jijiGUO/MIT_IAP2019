from compas.geometry import Line
from compas.plotters import Plotter

line = Line([0, 0, 0], [1, 1, 1])
mid_pt = line.midpoint
print(mid_pt)

plotter = Plotter(figsize=(10, 6))

lines = [{'start': line.start, 'end': line.end, 'width': 1.0}]
points = [{
    'pos': line.start,
    'radius': 0.05,
    'facecolor': '#ffffff',
    'text': 'start_point: {}'.format(line.start)
}]
points.append({'pos': mid_pt, 'radius': 0.05, 'facecolor': '#ff0000'})

plotter.draw_lines(lines)
plotter.draw_points(points)

plotter.show()
