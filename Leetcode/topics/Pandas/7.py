import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    for index, row in students.iterrows():
        if not row["name"]:
            students = students.drop(index)
    
    return students