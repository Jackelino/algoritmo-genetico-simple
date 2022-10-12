import math

from Chromosome import Chromosome


class Individual:

    def __init__(self, chromosomes: list, adn=''):
        """
        Individuo
        :param chromosome: cromosoma del individuo
        :param adn: adn del idividuo
        """
        if adn != '':
            self._adn = adn
            self._maps = self.mappingsInv(self.adn, chromosomes)  # valores mapeados del individuo c partir del adn
            self._values = self.getValues(self.maps, chromosomes)  # valores del individuo
            self._fitness = self.funtionsFitness(self.values)  # fitness evaluado del individuo
        else:
            self._values = self.initializeValues(chromosomes)  # valores del individuo
            self._maps = self.mappings(self.values, chromosomes)  # valores mapeados del individuo
            self._fitness = self.funtionsFitness(self.values)  # fitness evaluado del individuo
            self._adn = self.getADN(self.maps, chromosomes)

    def funtionsFitness(self, values: list):
        """
        conjunto de funciones a evaluar el individuo
        :param values: valores
        :return:
        """
        return self.f5(values)

    def f1(self, values: list):
        return (math.pow((1 - values[0]), 3) * math.e ** (- math.pow(values[0], 2) - math.pow((values[1] + 1), 3))) + (
                math.pow((1 - values[2]), 3) * math.e ** (- math.pow(values[0], 2) - math.pow((values[2] + 1), 3))) - (
                       values[0] - math.pow(values[0], 2) - math.pow(values[2], 2) * math.e ** (
                       - math.pow(values[1], 2) - math.pow(values[2], 2)))

    def f2(self, values: list):
        return math.pow(values[0], 3) - math.pow(values[0], 2) - values[0] + 2

    def f4(self, values: list):
        return (-0.000398 * values[0] + 0.001156 * values[1] + 0.000756 * values[2] + 0.000178 * values[3] + 0.001621 *
                values[4] + 0.000090 * values[5])

    def f5(self, values: list):
        return 0.5 + ((((math.sin((math.pow(values[0], 2) + math.pow(values[1], 2)) ** (0.5))) ** 2) - 0.5) / math.pow(
            1 + 0.001 * ((math.pow(values[0], 2) + math.pow(values[1], 2))), 2))

    def initializeValues(self, chromosomes: list):
        """
        inicializa los valores del individuo
        :param chromosomes: cromosomas
        :return: valores alearorios
        """
        values = []
        chromosome: Chromosome
        for chromosome in chromosomes:
            values.append(chromosome.generateRandomvalues(chromosome))
        return values

    def getValues(self, valuesMappings: list, chromosomes: list):

        values = []
        chromosome: Chromosome
        i = 0
        value: int
        for value in valuesMappings:
            chromosome = chromosomes[i]
            values.append(Chromosome.reverseMapping(chromosome.vMin, value, chromosome.precision))
            i = i + 1
        return values

    def mappings(self, values: list, chromosomes: list):
        """
        convierte los valores normales a valores mapeados
        :param values: valores normales enteros ó flotantes
        :param chromosomes: comosomas
        :return: valores mapeados
        """

        valuesMap = []
        chromosome: Chromosome
        chromosomeAux: Chromosome
        map = 0
        i = 0
        for value in values:
            chromosome = chromosomes[i]
            map = Chromosome.mapping(chromosome.vMin, value, chromosome.precision)
            valuesMap.append(map)
            i = i + 1
        return valuesMap

    def mappingsInv(self, adn: list, chromosomes: list):
        """
        convierte los valores de ADN a valores de tipo entero
        :param values: valores normales enteros ó flotantes
        :return: valores mapeados
        """
        valuesMap = []
        chromosome: Chromosome
        chromosomeAux: Chromosome
        i = 0
        for chromosome in chromosomes:
            strBinary = "".join(map(str, adn[i:i + chromosome.numberBits]))
            numberBinary = int(str(strBinary), 2)
            valuesMap.append(numberBinary)
            i = i + chromosome.numberBits
        return valuesMap

    def getADN(self, m: list, chromosomes: list):
        """
        optiene el adn del individuo
        :param m: valores mapeaos
        :param chromosomes: croosoma
        :return: retorna una lista cada posisxion es un bit [1,0,1]
        """
        adnString = ''
        adn = []
        chro: Chromosome
        c: Chromosome
        c2: Chromosome
        n: float
        i = 0
        for c in chromosomes:
            chro = c
            n = m[i]
            adnString += chro.getAdn(n, c)
            i = i + 1

        # lee la cadena de la conversion y la guarda en una lista
        for bit in adnString:
            adn.append(int(bit))
        return adn

    @property
    def adn(self):
        return self._adn

    # @adn.setter
    def set_adn(self, adn):
        self._adn = adn

    @property
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome(self, chromosome):
        self._chromosome = chromosome

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values

    @property
    def maps(self):
        return self._maps

    @maps.setter
    def maps(self, maps):
        self._maps = maps
