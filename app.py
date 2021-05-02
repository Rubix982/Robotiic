import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd

# Local imports
from controllers.GeneticDriverCode import GetGeneticDataframe


def GetData():
    __temp_df = pd.read_csv("./data/genetic.csv")
    del __temp_df["Unnamed: 0"]
    return __temp_df


def main():

    df = GetData()

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

    options = []
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

    st.write('''
    # N-Queens Using BackTracking

    There is an n x n grid where the value of n is 4≤n≤8 (user shall be asked at run time
    for the value of n he wants to keep). Your task is to place n queens on this board. As per the rules of
    chess, a queen should have no other queen in its respective column, neither should it have any other
    queen in its row nor should it have any within its diagonal cells. You can consider this case as placing
    each queen individually per column such that it does not violate any of the constraints mentioned. It’s
    quite easy to find solution manually but your task is now to code it and find the correct positions for the
    queens.

    This problem has to be solved through the concept of backtracking. So initially you will place the first
    queen randomly at any location within column 1. With respect to its location, now next n-1 queens’
    domain i.e. the places where they can be placed might shrink up.
    E.g. in this case 4 queens have to placed and Q1 is placed on (0,0) so x positions represent the illegal
    places now where other queens cannot be placed due to Q1 placement. This means for rest of the
    queens some positions have been considered as illegal.
    ''')

    st.image(Image.open('./assets/img/1.png'),
             caption='Sunrise by the mountains')

    st.write('''
    Further up, when we will move forward, there might be a point where domain gets empty for any
    particular queen, at that instance apply backtrack concept, which means that location of previous queen
    will have to get changed.
    Advise: Start building up your logic first on 4 queen problem so that you may exactly understand the
    flow then go for making a generalized code version of n queens’ placement.
    ''')

    st.write('''
    # Map Coloring using MRV and MCV

    Use Map given below and Assign colors using MRV and Degree Heuristic (MCV) Approach
    ''')

    st.image(Image.open('./assets/img/2.png'),
             caption='Sunrise by the mountains')


if __name__ == '__main__':
    main()
