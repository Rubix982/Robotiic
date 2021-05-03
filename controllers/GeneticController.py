import streamlit as st
import altair as alt
import pandas as pd

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