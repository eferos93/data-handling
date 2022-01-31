from pathlib import Path
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

def build_sample_name(df_sample_sheet):
    if df_sample_sheet["Sample_Name"].isnull().all():
        sample_names = df_sample_sheet["Sample_ID"].apply(lambda x : str(x)) + "_S" + df_sample_sheet["I7_Index_ID"].apply(lambda x : str(int(x[3:])))
        if not df_sample_sheet["Sample_Project"].isnull().all():
            sample_names = df_sample_sheet["Sample_Project"].apply(lambda x: str(x)) + "/" + sample_names

        return pd.DataFrame(sample_names, columns=["Sample_Name"])   
    else:
        sample_names = df_sample_sheet["Sample_Name"].apply(lambda x: str(x)) + "_S" + df_sample_sheet["Sample_Name"].apply(lambda x: str(x))
        if not df_sample_sheet["Sample_Project"].isnull().all():
            sample_names = df_sample_sheet["Sample_Project"].apply(lambda x: str(x)) + "/" + sample_names
        return pd.DataFrame(sample_names, columns=["Sample_Name"])

# given a dataframe with the [Data] contained in a sample sheet returns a dataframe with deduced sample names
def get_samples(file_name):
    df_ss = get_ss(file_name)
    # sn = df_ss["Sample_ID"].apply(lambda x : str(x)) + "_S" + df_ss["I7_Index_ID"].apply(lambda x : str(int(x[3:])))
    # df_samples = pd.DataFrame(sn, columns=["Sample_Name"])
    # return df_samples
    return build_sample_name(df_ss)

# argv[1] is the path to the sample_sheet, argv[2] the output path, argv[3] the filename
df_samples = get_samples(sys.argv[1])
output_path = Path(sys.argv[2])
output_path.mkdir(parents=True, exist_ok=True)
df_samples.to_csv(sys.argv[2] + '/' + sys.argv[3], index=False)

# get the names of the fastq files that will be produced, will be used then by fastqc
fastq_names = []
for row in df_samples.reset_index().itertuples():
    temp = {}
    for i in ["1", "2"]:
        temp["file" + i] = row.Sample_Name + "_R" + i + "_001.fastq.gz"
    fastq_names.append(temp)

json.dump(fastq_names, sys.stdout)