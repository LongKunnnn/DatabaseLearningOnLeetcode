import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = (
    person.groupby('email')
    .filter(lambda x: len(x) > 1)[['email']]
    .drop_duplicates()
    .reset_index(drop=True)
    )
    return df