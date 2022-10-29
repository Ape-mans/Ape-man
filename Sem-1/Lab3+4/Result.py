import pprint

from LUDecomposition import LUDecomposition
from Lab3.ReversedMatrixByLU import ReversedMatrixByLU

# A3 = [[1, 0, 3], [10, 4, 0], [3, 5, 4]]
# print("A 3x3:")
# pprint.pprint(A3)
#
# L, U = LUDecomposition.decompose_to_LU(A3)
#
# print("L:")
# pprint.pprint(L)
#
# print("U:")
# pprint.pprint(U)
#
# A4 = [[1, 0, 3, 5], [10, 4, 0, 6], [3, 5, 4, 7], [1, 2, 3, 7]]
# print("A 4x4:")
# pprint.pprint(A4)
#
# L, U = LUDecomposition.decompose_to_LU(A4)
#
# print("L:")
# pprint.pprint(L)
#
# print("U:")
# pprint.pprint(U)
#
# # 1
# startTime = time.time()  # время начала замера
#
# print(HilbertSolution.solve_LU(2))
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)

A = [[1, 2], [3, 4]]

L, U = LUDecomposition.decompose_to_LU(A)
Areversed = ReversedMatrixByLU.get_reversed(L, U)

pprint.pprint(A)
pprint.pprint(Areversed)

#
# # 2
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(50)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 3
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 2)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 5
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 3)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 6
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 4)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 7
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 5)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 8
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 6)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
