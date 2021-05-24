import streamlit as st
import altair as alt
import pandas as pd

def GeneticMainController(df: pd.DataFrame):

    MainProblemText()

    GenerateGeneticFrontend(df)

def MainProblemText():

    st.write('''
    # Exploring A Simple Genetic Algorithm

    In this assignment you will design and implement a simple genetic algorithm and explore its
    performance in evolving solution to one numerical problem, investigating the effect that various
    parameters have on its performance,

    1. Design and implement a simple genetic algorithm, in a language of your choice, to work on
    binary strings, and show its performance on the Max-1s problem where the aim is to get a
    chromosome of all 1s. Use an 8-bit chromosome and, when calculating the fitness, map the
    binary number onto an integer first; so the maximum fitness for an 8-bit chromosome is 255
    which is the ideal case to reach.

    2. Explore the performance of the algorithm as a function of population size and number of
    generations. Min and max number of population size to explore performance can be of your
    choice for e.g. min 4 and max 10

    3. Then increase the chromosome length and investigate/explore performance as a function of this
    length.

    By explore I mean you need to create a report in which graphs should be drawn to show how
    performance has varied with respect to population size, number of generations and chromosome length
    separately.

    Bear in mind that you will be using random number generators and that, to get a representative
    performance and results that are statistically significant, you will need to run each experiment several
    times.
    ''')    

def GenerateGeneticFrontend(df: pd.DataFrame):
    options = st.multiselect("Choose hyperparameters to graph", tuple(
        df.columns)[0:-1])

    options_selected = {}

    if "PopulationSize" in options:
        options_selected["PopulationSize"] = st.select_slider(
            'Specify population size',
            options=[*range(2, 16 + 1, 1)],
            value=(
                2,
                4))

    if "ChromosomeLength" in options:
        options_selected["ChromosomeLength"] = st.select_slider(
            'Specify chromosome length',
            options=[*range(8, 14 + 1, 1)],
            value=(
                8,
                12))

    if "ElitismFactor" in options:
        options_selected["ElitismFactor"] = st.select_slider(
            'Specify elitism factor',
            options=[*range(10, 20 + 1, 1)],
            value=(
                10,
                12))

    if "Iteration" in options:
        options_selected["Iteration"] = st.select_slider(
            'Specify iteration',
            options=[*range(1, 10 + 1, 1)],
            value=(
                1,
                5))
    __temp_df = df.copy()

    for key, value in options_selected.items():
        __temp_df = __temp_df[__temp_df[key] >= value[0]]
        __temp_df = __temp_df[__temp_df[key] <= value[1]]

    __temp_df = __temp_df.T.reset_index()

    __temp_df = pd.melt(__temp_df, id_vars=["index"]).rename(
        columns={"index": "Variables", "variable": "Iteration", "value": "Genetic Iterations"}
    )

    st.write("### Variables vs Genetic Iterations", __temp_df.sort_index())

    chart = (
        alt.Chart(__temp_df)
        .mark_area(opacity=0.3)
        .encode(
            x="Iteration:T",
            y=alt.Y("Genetic Iterations:Q", stack=None),
            color="Variables:N",
        )
    )
    st.altair_chart(chart, use_container_width=True)