import os
import pandas as pd

sample_dir = 'inputs/sample/'
sample_csv = sample_dir + 'salads_ml_use.csv'
sample_convert_csv = sample_dir + 'sample.csv'

# CSVがヘッダなしのため処理に注意
df = pd.read_csv(sample_csv, header=None)

flag_check_all = 0
for i, r in df.iterrows():
    # ファイル名を取得
    file_name = r[1]
    print(i, file_name)

    # 一致するファイル名を取得
    dir_files = os.listdir(sample_dir)
    flag_check = 0
    for dir_file in dir_files:
        if dir_file in file_name:
            flag_check = 1
            df.loc[i, 1] = "%s%s" % (sample_dir, dir_file)
            break

    if flag_check == 0:
        print('Error: Not Detect File.')
        flag_check_all = 1
        break

if flag_check_all == 0:
    print('Complete')
    df.to_csv(sample_convert_csv, header=False, index=False)
