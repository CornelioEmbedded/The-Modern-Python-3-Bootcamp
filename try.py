import pandas as pd
import numpy as np
import time



def generate_csv_file():

        df = pd.DataFrame(data =[["", "", "",""],
                                 ["", "", "",""],
                                 ["", "", "",""]],
                        index=['KNO', 'UFR', 'LFR'],
                        columns=['TLA','Current CPU Usage (%)', 
                                'Worst-case CPU Usage (%)', 
                                'Worst-case 50us task (%)'])
        df.to_csv(r"log\cpu_usage.csv", mode = 'w', index = True)
        return df


def add_csv_data(df, selection, current, worst_case, worst_case_50us):
    
    tla_dic = {0: 'KNO', 1: 'UFR', 2: 'LFR'}
    df.loc[[tla_dic[selection]],['Current CPU Usage (%)']] = current
    df.loc[[tla_dic[selection]],['Worst-case CPU Usage (%)']] = worst_case
    df.loc[[tla_dic[selection]],['Worst-case 50us task (%)']] = worst_case_50us

    df.to_csv(r"log\cpu_usage.csv", mode = 'w', index = True)

    
df = generate_csv_file()

add_csv_data(df,2,1,3,4)
