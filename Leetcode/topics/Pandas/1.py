import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
        return pd.DataFrame(student_data, columns=['student_id', 'age'])

# student_data = [
#     [1, 20],
#     [2, 22],
#     [3, 25],
#     [4, 21],
#     [5, 23]
# ]

# df = createDataframe(student_data)
# print("Test\n")
# print(df)