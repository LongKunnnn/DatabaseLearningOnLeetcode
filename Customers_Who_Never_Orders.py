import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_ids = orders['customerId']
    df = customers[~customers['id'].isin(ordered_ids)][['name']].reset_index(drop=True)
    df = df.rename(columns= {'name' : 'Customers'})
    return df