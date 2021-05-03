# Package imports
import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd

## Src Files
from src.EightQueens import NQueens

def EightQueensMainController(df: pd.DataFrame):

    MainProblemText()

    BoardSizeInputWithResult()

    # SpecifyBoardColAndRow()

    GenerateEightQueensFrontend(df)

def MainProblemText():
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
             caption='Chess board')

    st.write('''
    Further up, when we will move forward, there might be a point where domain gets empty for any
    particular queen, at that instance apply backtrack concept, which means that location of previous queen
    will have to get changed.
    Advise: Start building up your logic first on 4 queen problem so that you may exactly understand the
    flow then go for making a generalized code version of n queens’ placement.
    ''')

def BoardSizeInputWithResult():
    board_size = st.text_input('Board Size', '4')

    # NQueen driver code
    queens = NQueens(int(board_size))

    st.write(f'''
    The current board size is {board_size}, and the number of solutions are {queens.GenerateSolutions()}.
    _________________
    ''')       

    st.write(queens.board_text)

def SpecifyBoardColAndRow():
    st.write('''
    If you would like to specify the row and the column for the solutions to be generated
    ''')

    row = (st.number_input('Insert row'))

    column = st.number_input('Insert column')

    if row < 0 or row != int(row) or column < 0 or column != int(column):
        st.error('Please enter only valid')

    st.write(f'''
    The indexes specified include the {row}th row and {column}th column 
    ''')


def GenerateEightQueensFrontend(df: pd.DataFrame):
    st.write('''
    ## Graph results from dataset    

    Below are graphs for a generated dataset
    ''')

    options = st.selectbox("Choose a hyperparameter to graph", tuple(
        df.columns)[0:-1])

    options_selected = {}

    if "Size" in options:
        options_selected["Size"] = st.select_slider(
            'Specify board size',
            options=[*range(4, 8 + 1, 1)],
            value=(
                4,
                8))

    if "Time" in options:
        options_selected["Time"] = st.select_slider(
            'Specify time durat length',
            options=[1.0e-7, 1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1, 1],
            value=(
                1.0e-7,
                1.0e-1))

    __temp_df = df.copy()

    for key, value in options_selected.items():
        __temp_df = __temp_df[__temp_df[key] >= value[0]]
        __temp_df = __temp_df[__temp_df[key] <= value[1]]

    __temp_df = __temp_df.T.reset_index()

    __temp_df = pd.melt(__temp_df, id_vars=["index"]).rename(
        columns={"index": "Variables", "variable": "Iteration", "value": "Values"}
    )

    st.write("### Variables vs NQueens", __temp_df.sort_index())

    chart = (
        alt.Chart(__temp_df)
        .mark_area(opacity=0.3)
        .encode(
            x="Iteration:T",
            y=alt.Y("Values:Q", stack=None),
            color="Variables:N",
        )
    )
    st.altair_chart(chart, use_container_width=True) 
