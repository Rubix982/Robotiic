# Local imports
from controllers.Aux import GetGeneticData, GetQueensData, GenerateDataSetForFrontend
from controllers.EightQueensController import EightQueensMainController
from controllers.GeneticController import GeneticMainController
from controllers.GraphController import GraphMainController

def main():

    # Uncomment to generate the dataset
    # GenerateDataSetForFrontend()

    # Question 1
    GeneticMainController(GetGeneticData())

    # Question 2
    EightQueensMainController(GetQueensData())

    # Questions 3
    GraphMainController()

if __name__ == '__main__':
    main()
