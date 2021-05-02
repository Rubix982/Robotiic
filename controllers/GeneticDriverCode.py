# Package imports
import pandas as pd

# Local imports
from src.GeneticAlgorithm import GeneticAlgorithm

def GetGeneticDataframe():

    columns = ['PopulationSize', 'ChromosomeLength', 'ElitismFactor', 'Iteration', 'GeneticIterations']

    df = pd.DataFrame(columns=columns)

    # df = df.append(pd.DataFrame([[6, 8, 12, 3, 50]], columns=columns), ignore_index=True)

    # For population size
    for i in range(2, 15 + 1):

        # For Chromosome Length
        for j in range(8, 14):

            # For Elitism Factor
            for k in range(10, 20):

                # For each configuration, run
                # the algorithm exactly 10 times
                for w in range(0, 10):

                    genetic = GeneticAlgorithm(population_size=i, genes="10", target=("1" * j), elitismFactor=k)
                
                    df = df.append(pd.DataFrame([[i, j, k, w, genetic.GetIterations()]], columns=columns), ignore_index=True)

    df.to_csv('./data/genetic.csv')

    return df