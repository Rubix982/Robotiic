import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import networkx as nx
import altair as alt
import pandas as pd
import numpy as np

# Local imports

## Controllers
from controllers.EightQueensController import EightQueensMainController

from controllers.GeneticController import GeneticMainController
from controllers.GraphController import GraphMainController
from controllers.Aux import GetGeneticData, GetQueensData, GenerateDataSetForFrontend

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
