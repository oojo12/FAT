import pandas as pd
def prep_trans(filepath,outpath):
    trans_df = pd.read_excel(r'' + filepath,sheet_name="MASTER")

    state_dict = {
        'AK': 'Alaska', 'AL': 'Alabama','AR': 'Arkansas', 'AS': 'American Samoa',
        'AZ': 'Arizona','CA': 'California','CO': 'Colorado', 'CT': 'Connecticut',
        'DC': 'Washington D.C.','DE': 'Delaware', 'FL': 'Florida',
        'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa',
        'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas',
        'KY': 'Kentucky', 'LA': 'Louisiana','MA': 'Massachusetts', 'MD': 'Maryland',
        'ME': 'Maine', 'MI': 'Michigan','MN': 'Minnesota', 'MO': 'Missouri',
        'MP': 'Northern Mariana Islands','MS': 'Mississippi', 'MT': 'Montana',
        'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire',
        'NJ': 'New Jersey','NM': 'New Mexico', 'NV': 'Nevada','NY': 'New York',
        'OH': 'Ohio', 'OK': 'Oklahoma','OR': 'Oregon', 'PA': 'Pennsylvania',
        'PR': 'Puerto Rico', 'RI': 'Rhode Island','SC': 'South Carolina', 'SD': 'South Dakota',
        'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah','VA': 'Virginia', 'VI': 'Virgin Islands',
        'VT': 'Vermont','WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    columns = trans_df.columns.tolist()
    columns[8] = "State"
    trans_df.columns = columns

    trans_df['State'] = trans_df['State'].map(state_dict)
    trans_df.to_csv(r''+ outpath)
