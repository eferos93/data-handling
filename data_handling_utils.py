import pandas as pd
import sys
import json

# given the filename of a datasheet returns a dataframe containing the [Data] in the smaple sheet
def get_ss(file_name, tag='[Data]'):
    with open(file_name) as in_file:
        for line in in_file:
            if tag in line:
                break
        df = pd.read_csv(in_file)
    return df

# given a dataframe with the [Data] contained in a sample sheet returns a dataframe with deduced sample names
def get_samples(file_name):
    df_ss = get_ss(file_name)
    print(list(df_ss.columns.values))
    sn = df_ss["Sample_ID"].apply(lambda x : str(x))+"_S" + df_ss["I7_Index_ID"].apply(lambda x : str(int(x[3:])))
    df_samples = pd.DataFrame(sn, columns=["sample_name"])
    return df_samples

# argv[0] is the path to the sample_sheet, argv[1] the output path
df_samples = get_samples(sys.argv[0])
df_samples.to_csv(sys.argv[1], index=False)

# get the names of the fastq files that will be produced, will be used then by fastqc
fastq_names = []
for row in df_samples.reset_index().itertuples():
    temp = {}
    for i in ["1", "2"]:
        temp["file" + i] = row.sample_name + "_R" + i + "_001.fastq.gz"
    fastq_names.append(temp)

json.dump(fastq_names, sys.stdout)