from Chromosome import Chromosome
from Generation import Generation
from Individual import Individual

TYPE_VARIABLE = {
    "INTEGER": int,
    "FLOTANTE": float
}


def main():
    listChromosome = []
    # se crea el cromosoma con las valores
    c1 = Chromosome(0, 63, TYPE_VARIABLE.get("INTEGER"))
    c3 = Chromosome(0, 32, TYPE_VARIABLE.get("INTEGER"))
    c2 = Chromosome(-5.11, 5.12, TYPE_VARIABLE.get("FLOTANTE"), 2)
    listChromosome.append(c3)

    print("numero de bits a utilizar:", c3.numberBits)
    # listChromosome.append(c3)
    indi = Individual(listChromosome)
    """print(indi.values)
    print(indi.maps)
    print(indi.fitness)"""
    # se crea la generacion
    generation = Generation(6, "MAX", 0.5, 0.1, 4, listChromosome)
    print("----------------------------------------------------------------------------")
    print("Individuos\t Mapeados\t  AND\t Fitness")
    for generatio in generation.individuals:
        print(generatio.values, "\t", generatio.maps, "\t", generatio.adn, "\t", generatio.fitness)

    generation.generateNewIndividuals(generation)


main()
