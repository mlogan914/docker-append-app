import pandas as pd
import glob
import os

input_path = os.environ['INPUT_DIR']
output_path = os.environ['OUTPUT_DIR']

print(f'The INPUT path is {input_path}')
print(f'The OUTPUT path is {output_path}')

filename = 'all_years.csv'
csvs = glob.glob(os.path.join(input_path , "*.csv"))

li = []
for f in csvs:
    df = pd.read_csv(f, index_col=None, header=0)
    li.append(df)

df_concat = pd.concat(li,axis=0, ignore_index=True)

df_concat.to_csv(output_path+"/"+filename)

print("File is created sucessfully!")

## --- End of program code --##