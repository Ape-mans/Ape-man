import numpy as np
from matplotlib import pyplot as plt
from GradientDescent import GradientDescent
from StepConst import StepConst
from StepSplit import StepSplit
from StepFibonacci import StepFibonacci
from StepGoldenRatio import StepGoldenRatio
from ConjugateGradient import ConjugateGradient


def draw(a, b, func, points_x, points_y, name):
    fig, ax = plt.subplots()
    x, y = np.mgrid[a:b:100j, a:b:100j]
    ax.set_title(name)
    ax.contour(x, y, func([x, y]), levels=50, colors='#ccffff')
    for i in range(len(points_x)):
        ax.scatter(points_x[i], points_y[i], c='#ff0004')
    ax.plot([points_x[i] for i in range(len(points_x))], [points_y[i] for i in range(len(points_y))], c='#ff0004')
    plt.savefig(name + ".png")
    plt.show()


def func1(point):
    return point[0] ** 2 + 7 * point[1] ** 2 + point[0] * point[1] + 1


def func2(point):
    return 3 * point[0] ** 2 + 13 * point[1] ** 2


start_point1 = [1., 1.]
start_point2 = [-1., -1.]
step = 100
eps = 1e-7
func1_StepConst = GradientDescent.do_descent(func1, StepConst(step), eps, start_point1)
print(f"Name: func1_StepConst, Count of Steps: {func1_StepConst[0]}, Minimal_point: {func1_StepConst[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepConst[2]], [i[1] for i in func1_StepConst[2]], "func1_StepConst")

func1_StepSplit = GradientDescent.do_descent(func1, StepSplit(step, 0.5), eps, start_point1)
print(f"Name: func1_StepSplit, Count of Steps: {func1_StepSplit[0]}, Minimal_point: {func1_StepSplit[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepSplit[2]], [i[1] for i in func1_StepSplit[2]], "func1_StepSplit")

func1_StepFibonacci = GradientDescent.do_descent(func1, StepFibonacci(step), eps, start_point1)
print(f"Name: func1_StepFibonacci, Count of Steps: {func1_StepFibonacci[0]}, Minimal_point: {func1_StepFibonacci[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepFibonacci[2]], [i[1] for i in func1_StepFibonacci[2]],
     "func1_StepFibonacci")

func1_StepGoldenRatio = GradientDescent.do_descent(func1, StepGoldenRatio(step), eps, start_point1)
print(
    f"Name: func1_StepGoldenRatio, Count of Steps: {func1_StepGoldenRatio[0]}, Minimal_point: {func1_StepGoldenRatio[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepGoldenRatio[2]], [i[1] for i in func1_StepGoldenRatio[2]],
     "func1_StepGoldenRatio")

func1_ConjugateGradient = ConjugateGradient.do_descent(func1, StepGoldenRatio(step), eps, start_point1)
print(
    f"Name: func1_ConjugateGradient, Count of Steps: {func1_ConjugateGradient[0] - 1}, Minimal_point: {func1_ConjugateGradient[1]}")
draw(-2, 2, func1, [i[0] for i in func1_ConjugateGradient[2]], [i[1] for i in func1_ConjugateGradient[2]],
     "func1_ConjugateGradient")


func2_StepConst = GradientDescent.do_descent(func2, StepConst(step), eps, start_point2)
print(f"Name: func2_StepConst, Count of Steps: {func2_StepConst[0]}, Minimal_point: {func2_StepConst[1]}")
draw(-2, 2, func1, [i[0] for i in func2_StepConst[2]], [i[1] for i in func2_StepConst[2]], "func2_StepConst")

func2_StepSplit = GradientDescent.do_descent(func2, StepSplit(step, 0.5), eps, start_point2)
print(f"Name: func2_StepSplit, Count of Steps: {func2_StepSplit[0]}, Minimal_point: {func2_StepSplit[1]}")
draw(-2, 2, func1, [i[0] for i in func2_StepSplit[2]], [i[1] for i in func2_StepSplit[2]], "func2_StepSplit")

func2_StepFibonacci = GradientDescent.do_descent(func2, StepFibonacci(step), eps, start_point2)
print(f"Name: func2_StepFibonacci, Count of Steps: {func2_StepFibonacci[0]}, Minimal_point: {func2_StepFibonacci[1]}")
draw(-2, 2, func1, [i[0] for i in func2_StepFibonacci[2]], [i[1] for i in func2_StepFibonacci[2]],
     "func2_StepFibonacci")

func2_StepGoldenRatio = GradientDescent.do_descent(func2, StepGoldenRatio(step), eps, start_point2)
print(
    f"Name: func2_StepGoldenRatio, Count of Steps: {func2_StepGoldenRatio[0]}, Minimal_point: {func2_StepGoldenRatio[1]}")
draw(-2, 2, func2, [i[0] for i in func2_StepGoldenRatio[2]], [i[1] for i in func2_StepGoldenRatio[2]],
     "func2_StepGoldenRatio")

func2_ConjugateGradient = ConjugateGradient.do_descent(func2, StepGoldenRatio(step), eps, start_point1)
print(
    f"Name: func2_ConjugateGradient, Count of Steps: {func2_ConjugateGradient[0] - 1}, Minimal_point: {func2_ConjugateGradient[1]}")
draw(-2, 2, func2, [i[0] for i in func2_ConjugateGradient[2]], [i[1] for i in func2_ConjugateGradient[2]],
     "func2_ConjugateGradient")
