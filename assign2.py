import csv
import numpy as np

def f(w, b, x):
    return 1.0 / (1.0 + np.exp(-(w * x + b)))


def error(w, b):
    err = 0.0
    for x, y in reader:
        fx = f(w, b, x)
        err += 0.5 * (fx - y) ** 2
    return err


def grad_b(w, b, x, y):
    fx = f(w, b, x)
    return (fx - y) * fx * (1 - fx)


def grad_w(w, b, x, y):
    fx = f(w, b, x)
    return (fx - y) * fx * (1 - fx) * x


def do_gradient_descent():
    w, b, eta, max_epochs = 1, 1, 0.01, 100
    for i in range(max_epochs):
        dw, db = 0, 0
        with open('A2_Q4_data.csv', 'r') as csvFile:
            readr = csv.reader(csvFile)
            for x, y in readr:
                dw += grad_w(w, b, x, y)
                db += grad_b(w, b, x, y)
        w = w - eta * dw
        b = b - eta * db
    print(error(w, b))
    csvFile.close()


print("hi")
do_gradient_descent()
