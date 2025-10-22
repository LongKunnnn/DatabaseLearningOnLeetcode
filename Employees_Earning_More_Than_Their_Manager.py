import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    mgr = employee[['id', 'salary']].rename(columns= {'id' : 'managerId', 'salary' : 'managerSalary'})
    merged = employee.merge(mgr, on= 'managerId')
    result = merged[merged['salary'] > merged['managerSalary']]
    return result[['name']].rename(columns= {'name' : 'Employee'})
