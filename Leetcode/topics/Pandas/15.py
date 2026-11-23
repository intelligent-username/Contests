import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    over_100 = animals[animals['weight'] > 100].sort_values(by = 'weight', ascending = False)
    req_names = over_100["name"].to_frame()
    return req_names
