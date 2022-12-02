import json
import numpy as np


class SimplexMethod:
    def __init__(self):
        self.goal = None
        self.variables = []
        self.restrictions = []

    def _addNonOriginalVariable(self):
        self.variables.append(
            SimplexMethod.Variable(
                0,
                False))

    def _addOriginalVariable(self, coef: float):
        self.variables.append(
            SimplexMethod.Variable(
                coef,
                True))

    @staticmethod
    def solveFromJson(path: str):
        sis = SimplexMethod.Reader.FromJson(path)
        answers = []
        for si in sis:
            answers.append(SimplexMethod.SimplexTable(si).solve())
            print(answers)
        return answers

    class SimplexTable:
        def __init__(self, simplexInstance):
            self.si = simplexInstance
            self.coefs = []
            self.basis = []
            self.delta = []
            for r in self.si.restrictions:
                self.coefs.append(r.coefs + [r.answer])
            self.coefs = np.array(self.coefs, dtype=float)
            print(self.coefs)

        def _getDefaultBasis(self):
            return [-1 if not r.hasVariable else r.additionalVariableNumber for r in self.si.restrictions]

        def _noAnswerCondition(self, index):
            return np.max(self.coefs[:, index]) <= 0

        def _checkOptimality(self, indexWorstArgument):
            if self.si.goal == "Min":
                return self.delta[indexWorstArgument] <= 0
            elif self.si.goal == "Max":
                return self.delta[indexWorstArgument] >= 0

        def _getIndexWorstArgument(self):
            if self.si.goal == "Min":
                return np.argmax(self.delta[:-1])
            elif self.si.goal == "Max":
                return np.argmin(self.delta[:-1])

        def _createAnswer(self):
            answer = np.zeros(shape=(len(self.si.variables) - 1), dtype=float)
            for bi in range(len(self.basis)):
                answer[self._getBasisElement(bi)] = self.coefs[bi, -1]
            return [True, answer, self.delta[-1]]

        def _calculateDelta(self):
            self.delta = []
            for vi in range(len(self.si.variables)):
                self.delta.append(-1 * self.si.variables[vi].originalCoef)
                for ri in range(len(self.si.restrictions)):
                    self.delta[vi] += self.coefs[ri, vi] * self.si.variables[self.basis[ri]].originalCoef

        def _makeNewBasis(self, index):
            if self._noAnswerCondition(index):
                raise SimplexMethod.NoAnswerError.NoAnswer()
            i = np.argmax(self.coefs[:, index])
            self.basis[i] = index

        def _getBasisElement(self, basisIndex):
            if self.basis[basisIndex] != -1:
                return self.basis[basisIndex]
            self.basis[basisIndex] += 1
            while self.coefs[basisIndex, self.basis[basisIndex]] == 0:
                self.basis[basisIndex] += 1
            return self.basis[basisIndex]

        def solve(self):
            self.basis = self._getDefaultBasis()
            while True:
                for bi in range(len(self.basis)):
                    be = self._getBasisElement(bi)
                    coef = self.coefs[bi, be]
                    for ei in range(len(self.coefs[bi, :])):
                        self.coefs[bi, ei] /= coef
                    for bdi in range(len(self.basis)):
                        if bi == bdi:
                            continue
                        coef = self.coefs[bdi, be]
                        self.coefs[bdi, :] -= coef * self.coefs[bi, :]
                print(self.coefs)
                print(self.basis)
                self._calculateDelta()
                wdi = self._getIndexWorstArgument()
                if self._checkOptimality(wdi):
                    return self._createAnswer()
                else:
                    try:
                        self._makeNewBasis(wdi)
                    except SimplexMethod.NoAnswerError:
                        return [False]

    class Variable:
        def __init__(
                self,
                originalCoef: float,
                isOriginal: bool):
            self.originalCoef = originalCoef
            self.isOriginal = isOriginal

    class Restriction:
        def __init__(self, coefs, answer, additionalVariableNumber):
            self.coefs = coefs
            self.answer = answer
            if additionalVariableNumber != -1:
                self.hasVariable = True
                self.additionalVariableNumber = additionalVariableNumber
            else:
                self.hasVariable = False

        def updateForVariables(self, variables):
            for v in range(len(variables)):
                if not variables[v].isOriginal and self.hasVariable and self.additionalVariableNumber != v:
                    self.coefs.insert(v, 0)

        @staticmethod
        def getEqualRestriction(coefs, answer):
            return SimplexMethod.Restriction(coefs, answer, -1)

        @staticmethod
        def getGreaterRestriction(coefs, answer, variableNumber):
            coefs = [i * -1 for i in coefs] + [1]
            answer *= -1
            return SimplexMethod.Restriction(coefs, answer, variableNumber)

        @staticmethod
        def getLessRestriction(coefs, answer, variableNumber):
            coefs.append(1)
            return SimplexMethod.Restriction(coefs, answer, variableNumber)

    class Reader:
        @staticmethod
        def FromJson(path: str):
            with open(path, 'r') as json_data:
                data = json.load(json_data)
            tests = []
            for d in data["Tests"]:
                tests.append(SimplexMethod.Reader._parseTest(d))
            return tests

        @staticmethod
        def _parseTest(data):
            simplex = SimplexMethod()
            simplex.goal = data["Goal"]["Case"]
            for i in range(len(data["Goal"]["Coefs"])):
                simplex._addOriginalVariable(data["Goal"]["Coefs"][i])
            for i in data["Restrictions"]:
                if i["Case"] == "Equal":
                    simplex.restrictions.append(
                        SimplexMethod.Restriction.getEqualRestriction(
                            i["Coefs"],
                            i["Answer"]
                        )
                    )
                elif i["Case"] == "Less":
                    simplex.restrictions.append(
                        SimplexMethod.Restriction.getLessRestriction(
                            i["Coefs"],
                            i["Answer"],
                            len(simplex.variables)
                        )
                    )
                    simplex._addNonOriginalVariable()

                elif i["Case"] == "Greater":
                    simplex.restrictions.append(
                        SimplexMethod.Restriction.getGreaterRestriction(
                            i["Coefs"],
                            i["Answer"],
                            len(simplex.variables)
                        )
                    )
                    simplex._addNonOriginalVariable()

            for ri in range(len(simplex.restrictions)):
                simplex.restrictions[ri].updateForVariables(simplex.variables)
            simplex._addOriginalVariable(0)

            return simplex

    class NoAnswerError(Exception):
        def __init__(self, message):
            super().__init__(message)

        @staticmethod
        def NoAnswer():
            return SimplexMethod.NoAnswerError("No answer")
