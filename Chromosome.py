import math
import random


class Chromosome:

    def __init__(self, vMin: float, vMax: float, typeVar, precision=0):
        """
        cromosoma de cada individuo
        :param vMin: cota inferior
        :param vMax: cota superior
        :param typeVar: tipo de variable
        :param precision: decimales de presicion .00
        """
        self._vMin = vMin
        self._vMax = vMax
        self._precision = precision
        self._typeVar = typeVar
        self._numberBits = self.calculateNumberBits(self._vMin, self._vMax, self._precision)

    def calculateNumberBits(self, min: float, max: float, precision: int):
        """
        calcula el numero de bits utilizando presision si spn decoimales,  que utilizaremos para definir el cromosoma
        :param min: valor minimo
        :param max: valor maximo
        :return:
        """
        n = 1
        rango = ((max * math.pow(10, precision)) - (min * math.pow(10, precision))) + 1
        while (math.pow(2, n) < rango):
            n = n + 1
        return n

    def mapping(self, min: float, n: int, precision=0):
        """

        :param min:
        :param n:
        :param precision:
        :return:
        """
        if (precision != 0):
            return int((n * math.pow(10, precision)) - (min * math.pow(10, precision)))
        else:
            return n - min

    def reverseMapping(self, min: float, n: int, precision: int):
        """

        :param min:
        :param n:
        :return:
        """
        return (n + (min * math.pow(10, precision))) / math.pow(10, precision)

    def getAdn(self, n, chromosome):
        """
        convierte de el numero a su representacion binaria
        :param n: numero a convertir int|float
        :param chromosome: cromosoama
        :return:
        """
        return self.ajusteCeros(format(n, "b"), chromosome.numberBits)

    def ajusteCeros(self, s: str, n: int):
        """
        acompleta con ceros a la izquierda la cadena binaria
        :param s:
        :param n:
        :return:
        """
        if len(s) > n:
            return s[0:n]
        else:
            while len(s) < n:
                s = "0" + s
            return s

    def generateRandomvalues(self, chromosome):
        if chromosome.typeVar == int:
            return random.randint(chromosome.vMin, chromosome.vMax)
        if chromosome.typeVar == float:
            return round(random.uniform(chromosome.vMin, chromosome.vMax), chromosome.precision)

        return any

    @property
    def vMin(self):
        return self._vMin

    @vMin.setter
    def vMin(self, vMin):
        self._vMin = vMin

    @property
    def vMax(self):
        return self._vMax

    @vMax.setter
    def vMax(self, vMax):
        self._vMax = vMax

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, precision):
        self._precision = precision

    @property
    def typeVar(self):
        return self._typeVar

    @typeVar.setter
    def typeVar(self, typeVar):
        self._typeVar = typeVar

    @property
    def numberBits(self):
        return self._numberBits

    @numberBits.setter
    def numberBits(self, numberBits):
        self._numberBits = numberBits
