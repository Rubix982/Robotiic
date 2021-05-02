# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random

class FitnessCalculator():

    def __init__(self):
        pass

    @staticmethod
    def BinaryFitness(individual):

        __local_chromose_copy = individual.chromosome

        fitness, pow_factor = 0, len(__local_chromose_copy) - 1

        for i in range(0, len(__local_chromose_copy)):
            fitness += (int(__local_chromose_copy[i]) * ( 2 ** (pow_factor)))
            pow_factor -= 1 

        return fitness


class GnomeFactory():

    def __init__(self, genes: str, target: str):
        self.genes = genes
        self.target = target

    def MutateGenes(self):
        '''
        Create random genes for mutation
        '''

        return random.choice(self.genes)

    def CreateGnome(self):
        '''
        Create random genes for mutation
        '''

        return [self.MutateGenes() for _ in range(len(self.target))]


class Individual():
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome: str, Factory: GnomeFactory):
        self.chromosome = chromosome
        self.Factory = Factory
        self.fitness = self.CalFitness()

    def Mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''

        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            # random probability
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.Factory.MutateGenes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(
            child_chromosome,
            self.Factory)

    def CalFitness(self):
        '''
        Calculate fittness score, it is the number of
        characters in string which differ from target
        string.
        '''

        return FitnessCalculator.BinaryFitness(self)


class GeneticAlgorithm():

    def __init__(
            self,
            population_size: int,
            genes: str,
            target: str,
            elitismFactor: float = 10,
            logs: bool = False):

        # Set via constructor, public in scope
        self.population_size = population_size
        self.Factory = GnomeFactory(genes, target)
        self.elitismFactor = elitismFactor  # 10% of all 100% population
        self.logs = logs

        # Default params, private in scope
        self.__generation = 1  # init generation
        self.__found = False  # target found yet?
        self.__population = []  # actual population
        self.__desiredFitnessScore = FitnessCalculator.BinaryFitness(Individual(target, self.Factory))

    def GetIterations(self):

        # create initial population
        for _ in range(self.population_size):
            self.__population.append(
                Individual(
                    self.Factory.CreateGnome(),
                    self.Factory))

        while not self.__found:

            # sort the population in decreasing order of fitness score
            self.__population = sorted(self.__population, reverse=True, key=lambda x: x.fitness)

            # if the individual having lowest fitness score ie.
            # 0 then we know that we have reached to the target
            # and break the loop
            if self.__population[0].fitness == self.__desiredFitnessScore:
                found = True
                break

            # Otherwise generate new offsprings for new generation
            new_generation = []

            # Perform Elitism, that mean 10% of fittest population
            # goes to the next generation
            population_slice = int(
                (self.elitismFactor * self.population_size) / 100)

            new_generation.extend(self.__population[:population_slice])

            # From 50% of fittest population, Individuals
            # will mate to produce offspring
            population_slice = int(
                ((100 - self.elitismFactor) * self.population_size) / 100)

            for _ in range(self.population_size):
                parent1 = random.choice(self.__population[:50])
                parent2 = random.choice(self.__population[:50])
                new_generation.append(parent1.Mate(parent2))

            self.__population = new_generation

            if self.logs:
                print("Generation: {}\tString: {}\tFitness: {}".
                    format(self.__generation,
                            "".join(self.__population[0].chromosome),
                            self.__population[0].fitness))

            self.__generation += 1

        if self.logs:
            print("Generation: {}\tString: {}\tFitness: {}".
                format(self.__generation,
                        "".join(self.__population[0].chromosome),
                        self.__population[0].fitness))

        return self.__generation
