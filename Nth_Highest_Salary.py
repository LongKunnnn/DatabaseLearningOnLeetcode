import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    if employee.empty or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    

    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    
    if len(salaries) < N:
        result = None
    else:
        result = salaries.iloc[N - 1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})