# package imports
import pandas as pd
import time as tm

# Local imports
from src.EightQueens import NQueens

def GetNQueensDataFrame():

    columns = ['Size', 'Time', 'Solutions']

    df = pd.DataFrame(columns=columns)

    queens = NQueens()

    for i in range(4, 12 + 1):

        queens.SetSize(i)

        # Starting time
        start = tm.time()

        solutions = queens.GenerateSolutions()

        end = tm.time()

        df = df.append(pd.DataFrame([[i, end - start, solutions]], columns=columns), ignore_index=True)

    df.to_csv('./data/queens.csv', index=False)

    return df