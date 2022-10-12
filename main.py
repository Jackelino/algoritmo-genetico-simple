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


def main():
    listChromosome = []
    listGeneration = []
    # se crea el cromosoma con las valores
    c1 = Chromosome(0, 63, TYPE_VARIABLE.get("INTEGER"))
    c3 = Chromosome(0, 31, TYPE_VARIABLE.get("INTEGER"))
    c2 = Chromosome(-5.11, 5.12, TYPE_VARIABLE.get("FLOTANTE"), 2)
    listChromosome.append(c2)
    listChromosome.append(c2)
    print("numero de bits a utilizar:", c1.numberBits + c3.numberBits)

    """indi = Individual(listChromosome)
    indi2 = Individual(listChromosome, [0, 0, 0])
    print(indi2.values)
    print(indi2.maps)
    print(indi2.adn)
    print(indi2.fitness)"""
    # se crea la primera generacion
    generation = Generation(6, "MAX", 0.5, 0.1, 4, listChromosome, 1)
    listGeneration.append(generation)

    print("Numero de generacion: ", generation.nG)
    print("----------------------------------------------------------------------------")
    print("Individuos\t Mapeados\t  AND\t Fitness")
    for generatio in generation.individuals:
        print(generatio.values, "\t", generatio.maps, "\t", generatio.adn, "\t", generatio.fitness)
    print("Individuo de elite:")
    print(generation.eliteIndividual.values, "\t", generation.eliteIndividual.maps, "\t",
          generation.eliteIndividual.adn, "\t", generation.eliteIndividual.fitness)

    paro = 10
    i = 0
    bestGeneration = 1
    while i < paro - 1:
        generqacionNew = Generation(6, "MAX", 0.5, 0.1, 4, listChromosome, (i + 2), listGeneration[i],
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


def f1(values: list):
    return (math.pow((1 - values[0]), 3) * math.e ** (- math.pow(values[0], 2) - math.pow((values[1] + 1), 3))) + (
            math.pow((1 - values[2]), 3) * math.e ** (- math.pow(values[0], 2) - math.pow((values[2] + 1), 3))) - (
                   values[0] - math.pow(values[0], 2) - math.pow(values[2], 2) * math.e ** (
                   - math.pow(values[1], 2) - math.pow(values[2], 2)))


main()

