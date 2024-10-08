# https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# COMPLETE


import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['area'] >= 3000000) | (world['population'] >= 25000000)][['name', 'population', 'area']]
