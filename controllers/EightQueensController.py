import streamlit as st
import altair as alt
import pandas as pd

def GenerateEightQueensFrontend(df: pd.DataFrame):
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
