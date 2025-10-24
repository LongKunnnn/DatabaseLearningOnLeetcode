import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev1'] = logs['num'].shift(1)
    logs['prev2'] = logs['num'].shift(2)

    mask = (logs['num'] == logs['prev1']) & (logs['num'] == logs['prev2'])
    result = logs.loc[mask, 'num'].drop_duplicates().reset_index(drop=True)
    return pd.DataFrame({'ConsecutiveNums' : result})