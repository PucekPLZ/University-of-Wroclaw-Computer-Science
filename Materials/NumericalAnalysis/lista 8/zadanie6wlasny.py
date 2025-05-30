import matplotlib.pyplot as plt
import numpy as np

# Dane wejściowe

tk = [x/95 for x in range(96)]

x_data = [5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
6.5, 6.5, 5.5]

y_data = [41, 40.5, 40, 40.5, 41.5, 41.5, 42, 42.5, 43.5, 45, 47, 49.5, 53, 57, 59,
59.5, 61.5, 63, 64, 64.5, 63, 61.5, 60.5, 61, 62, 63, 62.5, 61.5, 60.5, 60, 59.5, 59, 58.5,
57.5, 55.5, 54, 53, 51.5, 50, 50, 50.5, 51, 50.5, 47.5, 44, 40.5, 36, 30.5, 28, 25.5, 21.5,
18, 14.5, 10.5, 7.50, 4, 2.50, 1.50, 2, 3.50, 7, 12.5, 17.5, 22.5, 25, 25, 25, 25.5, 26.5,
27.5, 27.5, 26.5, 23.5, 21, 19, 17, 14.5, 11.5, 8, 4, 1, 0, 0.5, 3, 6.50, 10, 13, 16.5, 20.5,
25.5, 29, 33, 35, 36.5, 39, 41]

# Funkcje sklejane trzeciego stopnia

def eval_lambda(x):
    lambdas = [0] # zeby indeksy sie zgadzaly
    for i in range(1, len(x)-1):
        lambdas.append((x[i] - x[i-1])/(x[i-1] + x[i+1]))
    return lambdas

def eval_h(x):
    h=[0]
    for i in range(1, len(x)):
        h.append(x[i] - x[i-1])
    return h

def eval_pq(lambdas):
    p = [0] # zeby indeksy sie zgadzaly
    q = [0]
    for i in range(1, len(lambdas)):
        p.append(lambdas[i]*q[i-1] + 2)
        q.append((lambdas[i] - 1)/p[i])
    return p, q

lamb = eval_lambda(tk)
p, q = eval_pq(lamb)
h = eval_h(tk)

def eval_d(x, y):
    d = [0] # zeby indeksy sie zgadzaly
    for i in range(1, len(x)-1):
        f1 = (y[i+1] - y[i]) / x[i+1] - x[i]
        f2 = (y[i] - y[i-1]) / x[i] - x[i-1]
        d.append(6*((f1-f2)/(x[i+1] - x[i-1])))
    return d

def eval_u(d, lamb, p):
    u = [0]
    for i in range(1, len(d)):
        u.append((d[i] - lamb[i]*u[i-1])/p[i])
    return u

def eval_m(u, q):
    M = [u[-1]]
    max = len(u)
    for i in range(1, max):
        M.append(u[max-i] + q[max-i]*M[i-1])
    M.append(0)
    M = M[::-1]
    return M

def eval_needed_for_s(x, y, p, q, lamb):
    d = eval_d(x, y)
    u = eval_u(d, lamb, p)
    m = eval_m(u, q)
    return d, u, m

def eval_sk(given_x, x, y, m, h, k):
    return ((1/6) * m[k-1] * (x[k] - given_x)**3
            + (1/6) * m[k] * (given_x - x[k-1])**3
            + (y[k-1] - (1/6) * m[k-1] * h[k]**2)*(x[k] - given_x)
            + (y[k] - (1/6) * m[k] * h[k]**2)*(given_x - x[k-1]))/h[k]

def eval_s(x, y, p, q, lamb, h, xs):
    d, u, m = eval_needed_for_s(x, y, p, q, lamb)
    ys = []
    i = 1
    for xk in xs:
        if (xk >= x[i-1]) and (xk <= x[i]):
            ys.append(eval_sk(xk, x, y, m, h, i))
        if xk > x[i]:
            i+=1
            ys.append(eval_sk(xk, x, y, m, h, i))
    return ys

dx, ux, mx = eval_needed_for_s(tk, x_data, p, q, lamb)
dy, uy, my = eval_needed_for_s(tk, y_data, p, q, lamb)

# Wybór M
M = 1000

a = [k/M for k in range(M+1)]

# Rysowanie

fig, ax = plt.subplots()

x = eval_s(tk, x_data, p, q, lamb, h, a)
y = eval_s(tk, y_data, p, q, lamb, h, a)

ax.plot(x, y, color = 'blue')

plt.show()