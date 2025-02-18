import matplotlib.pyplot as plt

def bernstein(i, n, t):
    coeff = 1

    for j in range(1, i + 1):
        coeff *= (n - j + 1) / j

    return coeff * (t ** i) * ((1 - t) ** (n - i))

def bezier_curve(control_points, weights, num_points=10000):
    n = len(control_points) - 1  

    t_values = [i / (num_points - 1) for i in range(num_points)]

    curve_points = []

    for t in t_values:
        x, y = 0, 0

        for i in range(n + 1):
            x += bernstein(i, n, t) * weights[i] * control_points[i][0]
            y += bernstein(i, n, t) * weights[i] * control_points[i][1]

        curve_points.append((x, y))

    return curve_points

control_points = [(0, 0), (3.5, 36), (25, 25), (25, 1.5), (-5, 3), (-5, 33), (15, 11), (-0.5, 35), (19.5, 15.5), (7, 0), (1.5, 10.5)]
weights = [1, 6, 4, 2, 3, 4, 2, 1, 5, 4, 1]

curve_points = bezier_curve(control_points, weights)

plt.plot([x for x, y in curve_points], [y for x, y in curve_points], color='blue')
plt.show()