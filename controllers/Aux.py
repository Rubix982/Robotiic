# Package imports
import streamlit as st
import pandas as pd

# Local imports
from controllers.GeneticDriverCode import GetGeneticDataframe
from controllers.EightQueensDriverCode import GetNQueensDataFrame

def DisplayNodePath(node_path_list: list):
    path = ''
    for i in range(0, len(node_path_list) - 1):
        path += f'{node_path_list[i]} -> '

    st.write(f'''
    >{path + node_path_list[-1]}
    ''')

def GetGeneticData():
    __temp_df = pd.read_csv("./data/genetic.csv")
    del __temp_df["Unnamed: 0"]
    return __temp_df

def GetQueensData():
    return pd.read_csv("./data/queens.csv")

def GenerateDataSetForFrontend():
    '''
    Generates the csv files, that is, the './data/genetic.csv' and the './data/queens.csv'
    '''

    # Generates the genetic dataset
    GetGeneticDataframe()

    # Generates the N Queens dataset
    GetNQueensDataFrame()