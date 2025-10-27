import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    df = weather.merge(
        weather, left_on= weather['recordDate'] - pd.Timedelta(days=1),
        right_on= 'recordDate',
        suffixes= ('_today', '_yesterday')
    )

    res = df[df['temperature_today'] > df['temperature_yesterday']][['id_today']]
    res.columns = ['id']
    return res