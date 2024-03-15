import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    emails = set()

    for index, row in customers.iterrows():
        if row["email"] in emails:
            customers = customers.drop(index)
        else:
            emails.add(row["email"])
    
    return customers
