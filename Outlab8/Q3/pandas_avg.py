# IMPLEMENTED BY: ASHWIN ABRAHAM

import pandas as pd

def read_data(file_name):
    r"""
        This function reads the contents from the file,
        specified by the file_name into a pandas DataFrame.
    """
    return pd.read_csv(file_name)

def compute_avg(data_frame: pd.DataFrame):
    r"""
        This function takes in a DataFrame and returns another 
        DataFrame with the computed averages
    """
    num_dict = {}
    cpi_dict = {}
    data_dict = {'programme': [], 'cgpa': []}
    for i in range(len(data_frame)):
        if data_frame.loc[i].programme in num_dict:
            num_dict[data_frame.loc[i].programme] += 1
            cpi_dict[data_frame.loc[i].programme] += data_frame.loc[i].cgpa
        else:
            num_dict[data_frame.loc[i].programme] = 1
            cpi_dict[data_frame.loc[i].programme] = data_frame.loc[i].cgpa
    for x in cpi_dict:
        cpi_dict[x] = cpi_dict[x]/num_dict[x]
        data_dict['programme'].append(x)
        data_dict['cgpa'].append(cpi_dict[x])
    rdf = pd.DataFrame.from_dict(data_dict)
    rdf.set_index('programme', inplace=True)
    return rdf


if __name__ == '__main__':
    df = read_data('example_input.csv')
    print('\n=============INPUT DF=============\n')
    print(df)
    print('\n=============EXPECTED OUTPUT=============\n')
    print(compute_avg(df))