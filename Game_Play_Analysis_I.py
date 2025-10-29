import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.copy()
    df['event_date'] = pd.to_datetime(df['event_date'])
    out = df.groupby('player_id', as_index=False)['event_date'].min()
    out = out.rename(columns={'event_date':'first_login'})
    return out[['player_id', 'first_login']]