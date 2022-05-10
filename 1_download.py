import os, subprocess
sample_dir = 'inputs/sample/'
sample_file = sample_dir + 'sample_file.txt'

# データの出力
f = open(sample_file, 'r')
datalist = f.readlines()
for i, data in enumerate(datalist):
    # データを取得
    file_name = data.strip()

    # 存在するファイルを確認
    dir_files = os.listdir(sample_dir)
    flag_check = 0
    for dir_file in dir_files:
        if dir_file in file_name:
            flag_check = 1
            break

    # 実行
    if flag_check:
        print(i, "Skip")
    else:
        string = "gsutil cp {0} {1}".format(file_name, sample_dir)
        print(i, string)
        subprocess.call(string, shell=True)

f.close()
