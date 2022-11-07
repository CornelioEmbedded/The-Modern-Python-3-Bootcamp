import pandas as pd
import time


def generate_csv(selection, current, worst_case, worst_case_50us):
    
    FORMAT = 'w'

    tla_dic = {0: 'KNO', 1: 'UFR', 2: 'LFR'}

    df = pd.DataFrame(data =  [["", "", ""],
                               ["", "", ""],
                               ["", "", ""]],
                      index=['KNO', 'UFR', 'LFR'],
                      columns=['Current CPU Usage (%)', 
                               'Worst-case CPU Usage (%)', 
                               'Worst-case 50us task (%)'])

    df.loc[[tla_dic[selection]],['Current CPU Usage (%)']] = current
    df.loc[[tla_dic[selection]],['Worst-case CPU Usage (%)']] = worst_case
    df.loc[[tla_dic[selection]],['Worst-case 50us task (%)']] = worst_case_50us

    df.to_csv(r"log\cpu_usage.csv", mode = FORMAT, index = True)

for i in range(3):
    generate_csv(i,1,1,1)
    time.sleep(1)
