from cvxopt import matrix, solvers, spmatrix
import numpy as np
import matplotlib.pyplot as plt
from math import *

def main():
    data = [[3.0,5,1], [5,3,1], [6,6,1], [5,6,-1], [6,5,-1]]
    l=len(data)
    Q = spmatrix(2.0, range(8), range(8))
    Q[2,2] = 0
    Q[3,3] = 0
    Q[4,4] = 0
    Q[5,5] = 0
    Q[6,6] = 0
    Q[7,7] = 0
    p = matrix([0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0], (8,1))
    G = []
    h = []
    G_vec = [[-1.0, 0.0, 0.0, 0.0, 0.0], [0.0, -1.0, 0.0, 0.0, 0.0], [0.0, 0.0, -1.0, 0.0, 0.0], [0.0, 0.0, 0.0, -1.0, 0.0], [0.0, 0.0, 0.0, 0.0, -1.0]]
    G_vec2 = [[0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]]
    ctr=0
    for items in data:
        row = []
        if items[2] == 1:
            row.extend([-1 * item for item in items[:2]])
            row.append(-1)
            row.extend(G_vec[ctr])
            G.append(row)
            h.append(-1.0)
        else:
            row.extend(items[:2])
            row.append(1)
            row.extend(G_vec[ctr])
            G.append(row)
            h.append(-1.0)
        ctr=ctr+1
        if items == data[l-1]:
            for i in range(5):
                G.append(G_vec2[i])
                h.append(0)


    G = matrix(G).trans()
    h = matrix(h)
    A = None
    b = None
    sol=solvers.qp(Q, p, G, h)
    w1 = sol['x'][0]
    w2 = sol['x'][1]
    b  = sol['x'][2]
    print 'w1= {0}; w2={1}; b={2}'.format(w1, w2, b)

    ### suppose you have obtained sol['x'] from CVXOPT QP minimization

    x = [item[0] for item in data if item[2] == 1]
    y = [item[1] for item in data if item[2] == 1]
    plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
    x = [item[0] for item in data if item[2] == -1]
    y = [item[1] for item in data if item[2] == -1]
    plt.scatter(x, y, s=80, facecolors='none', edgecolors='b')
    x = [item[0] for item in data]
    y = [item[1] for item in data]
    plt.scatter(x, y, s=40, facecolors='none', edgecolors='k')
    w1 = sol['x'][0]
    w2 = sol['x'][1]
    b = sol['x'][2]

    print 'Answer to question a:'
    print 'w: {0}; b: {1} \n'.format([w1,w2], b)
    print 'Answer to question b:'
    for point in data:
        print '{0}: {1}'.format(point, abs(w1 * point[0] + w2 * point[1] + b)/sqrt(w1 * w1 + w2 * w2))

    print '\nAnswer to question c: '
    print 2/sqrt(w1 * w1 + w2 * w2)

    print '\nAnswer to question d:'
    print 'w.x + b > 0 for positive class'
    print 'w.x + b < 0 for negative class'

    x = [min([item[0] for item in data]), max([item[0] for item in data])]

    y = [(w1 * x[i] + b)/(-1 * w2) for i in range(2)]

    plt.plot(x, y, color='red')

    y = [(w1 * x[i] + b - 1)/(-1 * w2) for i in range(2)]

    plt.plot(x, y, color='black')

    y = [(w1 * x[i] + b + 1)/(-1 * w2) for i in range(2)]

    plt.plot(x, y, color='black')

    plt.gca().set_aspect('equal', adjustable='box')

    plt.grid()

    plt.show()


if __name__ == '__main__':
    print 'Non-Separable SVM program'
    main()