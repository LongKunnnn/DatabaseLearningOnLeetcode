import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().nlargest(2)
    return pd.DataFrame({'SecondHighestSalary' : [salaries.iloc[-1] if len(salaries) == 2 else None]})