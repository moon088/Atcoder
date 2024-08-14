import os
import sys


default_output_directory = 'AtCoder\Working'
num_files_to_generate = 4  # 生成するファイルの個数（デフォルトは4個）
output_directory = default_output_directory

if len(sys.argv) >= 2:
    num_files_to_generate = int(sys.argv[1])

if len(sys.argv) == 3:
    output_directory = sys.argv[2]

# テンプレートファイルのパス
template_path = 'AtCoder\Template.py'

# 生成するファイル名と対応するコメントのリスト
files = ['A.py', 'B.py', 'C.py', 'D.py', 'E.py', 'F.py']
comments = ['# A', '# B', '# C', '# D', '# E', '# F']

#files =[".py", ".py", ".py", ".py"]

with open(template_path, 'r',  encoding='utf-8') as template_file:
    template_content = template_file.read()



for filename, comment in zip(files[:num_files_to_generate], comments[:num_files_to_generate]):
    output_path = os.path.join(output_directory, filename)
    with open(output_path, 'w') as new_file:
        new_file.write(f"{comment}\n{template_content}")