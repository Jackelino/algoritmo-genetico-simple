import random

from Individual import Individual


class Generation:

    def __init__(self, population: int, optimization: str, pC: float, pM: float, selection: int,
                 chromosome: list, nG: int,
                 generation=0, mutation=-1):
        """
        Genaraxcion
        :param population: tamaño de la poblacion
        :param optimization:
        :param pC: porcentaje de cruza
        :param pM: porcentaje de mutacion
        :param selection: numero de inividuos a sleccionar de cada generacion
        :param chromosome: cromosomas del inidividuo
        :param nG: numero de generacion
        :param generation: gemeracion siguiente
        :param mutation: tipo de mutacion
        """
        self._nG = nG
        self._population = population
        self._optimization = optimization
        self._pC = pC
        self._pM = pM
        self._mutation = mutation
        self._selection = selection
        self._chromosome = chromosome
        self._error = 0  # error de la generacion
        if generation == 0:
            self._individuals = self.generateFirstGenearation(chromosome, self.population)  # individuos
        else:
            self._individuals = self.generateNewIndividuals(generation)
        # self._fit = self.fit  # fitness de la generacion
        self._eliteIndividual = self.selectBestfitness(self.individuals, self.optimization)
        self._precision = 0  # presicion

    def generateFirstGenearation(self, chromosomes: list, population: int):
        """
        genera la primera generacion
        :param chromosomes: cromosomas del individuo
        :param population: numero de genearciones a generar
        :return:
        """
        individuals = []
        for n in range(0, population):
            individual = Individual(chromosomes)
            individuals.append(individual)
        return individuals

    def generateNewIndividuals(self, generation):
        """
        genera a los nuevos individuos de la siguiente generacion
        :param generation: genracion actual
        :return:
        """
        individuals = []
        individualsOrder = list()
        individualsSelection = list()
        g: Generation = generation
        chromosome: list = g.chromosome
        hijo: Individual
        # ordena
        individualsOrder = self.orderIndividual(g.individuals, g.optimization)
        # selecciona
        for individual in range(0, g.selection - 1):
            individualsSelection.append(individualsOrder[individual])
        # cruza
        ban = True
        i = g.selection - 1
        while ban:
            if len(individuals) == g.population:
                break
            hijo = Individual(chromosome,
                              self.crosses(individualsSelection[i - i], individualsSelection[i - (i - 1)], g.pC, g.pM,
                                           0))
            individuals.append(hijo)
            if len(individuals) == g.population:
                break
            hijo = Individual(chromosome,
                              self.crosses(individualsSelection[i - i], individualsSelection[i - (i - 2)], g.pC, g.pM,
                                           1))
            individuals.append(hijo)
            if len(individuals) == g.population:
                break
            hijo = Individual(chromosome,
                              self.crosses(individualsSelection[i - i], individualsSelection[i - 1], g.pC, g.pM,
                                           2))
            individuals.append(hijo)
            if len(individuals) == g.population:
                break
            hijo = Individual(chromosome,
                              self.crosses(individualsSelection[i - i], individualsSelection[i - (i - 1)], g.pC, g.pM,
                                           3))
            individuals.append(hijo)
        return individuals

    def crosses(self, father: Individual, mother: Individual, pC: float, pM: float, option: int):
        position1 = int(len(father.adn) * pC)
        position2 = len(father.adn) - position1
        adn = []

        if option == 0:
            adn = father.adn[0:position1] + mother.adn[position1:]
        elif option == 1:
            adn = mother.adn[0:position1] + father.adn[position1:]
        elif option == 2:
            adn = father.adn[0:position2] + mother.adn[position2:]
        elif option == 3:
            adn = mother.adn[0:position2] + father.adn[position2:]

        adn = self.mutations(adn, self.mutation)

        return adn

    def mutations(self, adn: list, option: int):
        if option == 0:
            return self.randomlyMutate(adn)
        elif option == 1:
            return self.mutateByBit(adn)

    def randomlyMutate(self, adn: list):
        """
        muta el adn de un individuo de forma aleatoria
        :param adn: adn de individuo a mutar
        :return: retorna el adn mutado del indivoduo
        """
        numberRandomAnd: int
        individualMutado: Individual

        adnMutado = adn

        numberRandomAnd = random.randint(0, len(adn) - 1)

        if adnMutado[numberRandomAnd] == 1:
            adnMutado[numberRandomAnd] = 0
        else:
            adnMutado[numberRandomAnd] = 1

        return adnMutado

    def mutateByBit(self, adn: list):
        """
        muta el adn del bit menos significativo
        :param adn: adn de individuo a mutar
        :return: retorna el adn mutado del indivoduo
        """
        adnMutado = adn

        if adnMutado[len(adnMutado) - 1] == 1:
            adnMutado[len(adnMutado) - 1] = 0
        else:
            adnMutado[len(adnMutado) - 1] = 1

        return adnMutado

    def selectBestfitness(self, indivisuals: list, optimization: str):
        """
        selecciona el mejor individuo con partir de la optimizacion
        :param fitness: lista de fitnes de los inidividuos
        :param optimization: tipo de optimizacion MAX MIN
        :return: retorna el mejor inidividuo
        """
        individual: Individual
        value = 0
        fitness = []
        for individual in indivisuals:
            fitness.append(individual.fitness)

        if optimization == "MAX":
            value = max(fitness)
        if optimization == "MIN":
            value = min(fitness)
        indexValue = fitness.index(value)
        individual = self.individuals[indexValue]
        return individual

    def orderIndividual(self, individuals: list, optimization: str):
        """
        ordena a los idividuos de la genracion
        :param individuals: individuos actuales de la genracion
        :param optimization:
        :return: retorna una lista de mos inidividuos ordenados
        """
        individualsOrder = []
        if optimization == "MAX":
            individualsOrder = sorted(individuals, key=lambda x: x.fitness, reverse=True)
        if optimization == "MIN":
            individualsOrder = sorted(individuals, key=lambda x: x.fitness)

        return individualsOrder

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population

    @property
    def optimization(self):
        return self._optimization

    @optimization.setter
    def optimization(self, optimization):
        self._optimization = optimization

    @property
    def eliteIndividual(self):
        return self._eliteIndividual

    @eliteIndividual.setter
    def eliteIndividual(self, eliteIndividual):
        self._eliteIndividual = eliteIndividual

    @property
    def individuals(self):
        return self._individuals

    @individuals.setter
    def individuals(self, individuals):
        self._individuals = individuals

    @property
    def fit(self):
        return self._fit

    def set_fit(self, fit):
        self._fit = fit

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, selection):
        self._selection = selection

    @property
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome(self, chromosome):
        self._chromosome = chromosome

    @property
    def mutation(self):
        return self._mutation

    @mutation.setter
    def mutation(self, mutation):
        self._mutation = mutation

    @property
    def pC(self):
        return self._pC

    @pC.setter
    def pC(self, pC):
        self._pC = pC

    @property
    def pM(self):
        return self._pM

    @pM.setter
    def pM(self, pM):
        self._pM = pM

    @property
    def nG(self):
        return self._nG

    @nG.setter
    def nG(self, nG):
        self._nG = nG
