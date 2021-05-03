# Package imports
import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd

# Local imports
from controllers.GraphDriver import GraphDriver
from controllers.Aux import DisplayNodePath

def GraphMainController():

    MainProblemText()

    GraphDriver()

    GraphLogic()

def MainProblemText():
    st.write('''
    # Map Coloring using MRV and MCV

    Use Map given below and Assign colors using MRV and Degree Heuristic (MCV) Approach
    ''')

    st.image(Image.open('./assets/img/2.png'),
             caption='Pakistan\' geographical map')

def GraphLogic():
    generated_graph_paths = GraphDriver()

    st.image(Image.open('./assets/img/Pakistan.png'),
        caption='Pakistan Graph Representation')

    DisplayNodePath(generated_graph_paths['mrv'])

    st.image(Image.open('./assets/img/MRV.png'),
        caption='MRV Graph')

    DisplayNodePath(generated_graph_paths['mcv'])

    st.image(Image.open('./assets/img/MCV.png'),
        caption='MCV Graph')
