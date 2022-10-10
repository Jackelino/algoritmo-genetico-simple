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
    listChromosome.append(c1)

    print("numero de bits a utilizar:", c1.numberBits)
    # listChromosome.append(c3)
    """indi = Individual(listChromosome)
    indi2 = Individual(listChromosome, [0, 0, 0])
    print(indi2.values)
    print(indi2.maps)
    print(indi2.adn)
    print(indi2.fitness)"""
    # se crea la generacion
    generation = Generation(6, "MAX", 0.5, 0.1, 4, listChromosome)
    print("----------------------------------------------------------------------------")
    print("Individuos\t Mapeados\t  AND\t Fitness")
    for generatio in generation.individuals:
        print(generatio.values, "\t", generatio.maps, "\t", generatio.adn, "\t", generatio.fitness)

    generqacion2 = Generation(6, "MAX", 0.5, 0.1, 4, listChromosome, generation)
    print("----------------------------------------------------------------------------")
    print("Individuos\t Mapeados\t  AND\t Fitness")
    for generatio in generqacion2.individuals:
        print(generatio.values, "\t", generatio.maps, "\t", generatio.adn, "\t", generatio.fitness)


main()
