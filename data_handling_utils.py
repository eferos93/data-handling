import pandas as pd
import sys

# given the filename of a datasheet returns a dataframe containing the [Data] in the smaple sheet
def get_ss(file_name, tag='[Data]'):
    with open(file_name) as in_file:
        for line in in_file:
            if tag in line:
                break
        df=pd.read_csv(in_file)
    return df

# given a dataframe with the [Data] contained in a sample sheet returns a dataframe with deduced sample names
def get_samples(file_name):
    df_ss = get_ss(file_name)
    sn=df_ss["Sample_ID"].apply(lambda x : str(x))+"_S"+df_ss["I7_Index_ID"].apply(lambda x : str(int(x[3:])))
    df_samples=pd.DataFrame(sn, columns=["sample_name"])
    return df_samples

get_samples(sys.argv[0]).to_csv(sys.argv[1], index=False)