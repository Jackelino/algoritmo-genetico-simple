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
            self._maps = self.mappingsInv(self.adn)  # valores mapeados del individuo c partir del adn
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
        return self.f1(values)

    def f1(self, values: list):
        return values[0] + 5

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
            values.append(chromosome.reverseMapping(chromosome.vMin, value, chromosome.precision))
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
            map = chromosome.mapping(chromosome.vMin, value, chromosome.precision)
            valuesMap.append(map)
            i = i + 1
        return valuesMap

    def mappingsInv(self, adn: list):
        """
        convierte los valores de ADN a valores de tipo entero
        :param values: valores normales enteros ó flotantes
        :return: valores mapeados
        """
        valuesMap = []
        chromosome: Chromosome
        chromosomeAux: Chromosome
        strBinary = "".join(map(str, adn))
        numberBinary = int(str(strBinary), 2)
        valuesMap.append(numberBinary)
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
        n: float
        i = 0
        for c in chromosomes:
            chro = c
            n = m[i]
            adnString += c.getAdn(n, chro)
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
