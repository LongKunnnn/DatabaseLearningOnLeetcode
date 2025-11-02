import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_counts = (
        employee[employee['managerId'].notna()]
        .groupby('managerId')
        .size()
        .reset_index(name='count')
    )

    managers = report_counts[report_counts['count'] >= 5]

    result = employee[employee['id'].isin(managers['managerId'])][['name']]

    return result