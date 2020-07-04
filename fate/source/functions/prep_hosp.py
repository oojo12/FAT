import pandas as pd
def prep_hosp(filepath,outpath):
    hos_stats.read_csv(filepath)
    states = hos_stats['State'].tolist()

    for i in range(len(states)):
        states[i] = states[i][0:2]

    hos_stats['State'] = states
    
    hos_stats.to_csv(r'' + outpath)