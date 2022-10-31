import math

from Chromosome import Chromosome
from Generation import Generation

TYPE_VARIABLE = {
    "INTEGER": int,
    "FLOTANTE": float
}
TYPE_MUTATIONS = {
    "ALEATORIA": 0,
    "BIT_MENOS_SIGNIFICATIVO": 1
}

TYPE_OPTIMIZATION = {
    "MAX": "MAX",
    "MIN": "MIN"
}

POPULATION = 10
CROSSOVER_RATE = 0.5
MUTATION_RATE = 0.1
GENERATION_NUMBER = 10


def main():
    listChromosome = []
    listGeneration = []
    # se crea el cromosoma con las valores
    c1 = Chromosome(0, 63, TYPE_VARIABLE.get("INTEGER"))
    c3 = Chromosome(0, 31, TYPE_VARIABLE.get("INTEGER"))
    c2 = Chromosome(-5.11, 5.12, TYPE_VARIABLE.get("FLOTANTE"), 2)
    listChromosome.append(c1)
    print("numero de bits a utilizar:", c2.numberBits)
    # se crea la primera generacion
    generation = Generation(POPULATION, TYPE_OPTIMIZATION.get("MAX"), CROSSOVER_RATE, MUTATION_RATE, 4, listChromosome, 1)
    listGeneration.append(generation)

    print("Numero de generacion: ", generation.nG)
    print("----------------------------------------------------------------------------")
    print("Individuos\t Mapeados\t  AND\t Fitness")
    for generatio in generation.individuals:
        print(generatio.values, "\t", generatio.maps, "\t", generatio.adn, "\t", generatio.fitness)
    print("Individuo de elite:")
    print(generation.eliteIndividual.values, "\t", generation.eliteIndividual.maps, "\t",
          generation.eliteIndividual.adn, "\t", generation.eliteIndividual.fitness)

    i = 0
    bestGeneration = 1
    while i < GENERATION_NUMBER - 1:
        generqacionNew = Generation(POPULATION, TYPE_OPTIMIZATION.get("MAX"), CROSSOVER_RATE, MUTATION_RATE, 4, listChromosome, (i + 2),
                                    listGeneration[i],
                                    TYPE_MUTATIONS.get("ALEATORIA"))
        listGeneration.append(generqacionNew)
        print("Numero de generacion: ", generqacionNew.nG)
        print("----------------------------------------------------------------------------")
        print("Individuos\t Mapeados\t  AND\t Fitness")
        for individual in generqacionNew.individuals:
            print(individual.values, "\t", individual.maps, "\t", individual.adn, "\t", individual.fitness)

        print("Individuo de elite:")
        print(generqacionNew.eliteIndividual.values, "\t", generqacionNew.eliteIndividual.maps, "\t",
              generqacionNew.eliteIndividual.adn, "\t", generqacionNew.eliteIndividual.fitness)
        if listGeneration[i].eliteIndividual.fitness < generqacionNew.eliteIndividual.fitness:
            bestGeneration = generqacionNew.nG
        print("Mejor generacion: ", bestGeneration)
        i = i + 1
        print("----------------------------------------------------------------------------")


main()
