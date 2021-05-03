import streamlit as st

def DisplayNodePath(node_path_list: list):
    path = ''
    for i in range(0, len(node_path_list) - 1):
        path += f'{node_path_list[i]} -> '

    st.write(f'''
    >{path + node_path_list[-1]}
    ''')
