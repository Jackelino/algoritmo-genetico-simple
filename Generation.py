from Individual import Individual


class Generation:

    def __init__(self, population: int, optimization: str, pC: float, pM: float, selection: int, chromosome: list):
        """
        Generacion
        :param population: tamaño de la poblacion
        :param optimization: optimizacion MAX | MIN de la funcion a optimizar
        :param pC: porcentaje de cruza
        :param pM: porcentaje de mutacion
        :param selection: cuantos individuos seran seleccionado
        :param chromosome: Cromosomas
        """
        self._population = population
        self._optimization = optimization
        self._pC = pC
        self._pM = pM
        self._selection = selection
        self._chromosome = chromosome
        self._nG = 0  # numero de generacion
        self._error = 0  # error de la generacion
        self._individuals = self.generateFirstGenearation(chromosome, self.population)  # individuos
        self._fit = self.fit  # fitness de la generacion
        self._eliteIndividual = self.selectBestfitness(self.fit, self.optimization)
        self._precision = 0  # presicion

    def generateFirstGenearation(self, chromosomes: list, population: int):
        """
        genera la primera generacion
        :param chromosomes: cromosomas del individuo
        :param population: numero de genearciones a generar
        :return:
        """
        individuals = []
        fit = []
        for n in range(0, population):
            individual = Individual(chromosomes)
            fit.append(individual.fitness)
            individuals.append(individual)
        self.set_fit(fit)
        return individuals

    def generateNewIndividuals(self, generartion):
        individuals = []
        individualsOrder = list()
        g: Generation = generartion
        hijo: Individual
        # ordena
        individualsOrder = self.orderIndividual(g.individuals, g.optimization)
        # selecciona
        for individual in range(0, g.selection):
            individuals.append(individualsOrder[individual])
        #cruza
        self.cruza()


    def cruza(self, father: Individual, mother: Individual, pC, pM, option: int):
        pass

    def mutacion(self):
        pass

    def selectBestfitness(self, fitness: list, optimization: str):
        """
        selecciona el mejor individuo con partir de la optimizacion
        :param fitness: lista de fitnes de los inidividuos
        :param optimization: tipo de optimizacion MAX MIN
        :return: retorna el mejor inidividuo
        """
        individual: Individual
        value = 0
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
