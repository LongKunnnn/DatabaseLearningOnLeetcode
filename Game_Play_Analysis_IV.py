import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.rename(columns={'event_date':'first_login'}, inplace=True)

    df = activity.merge(first_login, on='player_id')
    df['next_day'] = df['event_date'] == df['first_login'] + pd.Timedelta(days=1)
    player_next_day = df.groupby('player_id')['next_day'].max().reset_index()
    fraction = player_next_day['next_day'].mean()
    return pd.DataFrame({'fraction' : [round(fraction, 2)]})