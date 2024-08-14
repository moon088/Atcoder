import os
import sys

default_output_directory = 'AtCoder\Working'
num_files_to_generate = 1  # 生成するファイルの個数（デフォルトは4個）
output_directory = default_output_directory

if len(sys.argv) >= 2:
    num_files_to_generate = int(sys.argv[1])

if len(sys.argv) == 3:
    output_directory = sys.argv[2]

# テンプレートファイルのパス
template_path = 'AtCoder\Template.py'

# 標準入力からファイル名とコメントの入力を受け取る
files = []
comments = []

for i in range(num_files_to_generate):
    filename = input(f"ファイル名の入力") + ".py"
    comment = input(f"難易度の入力")
    files.append(filename)
    comments.append(f"# {comment}")

# テンプレートファイルの内容を読み込む
with open(template_path, 'r') as template_file:
    template_content = template_file.read()

# 指定されたファイル名とコメントで新しいファイルを生成
for filename, comment in zip(files, comments):
    output_path = os.path.join(output_directory, filename)
    os.makedirs(output_directory, exist_ok=True)  # 出力ディレクトリが存在しない場合は作成
    with open(output_path, 'w') as new_file:
        new_file.write(f"{comment}\n{template_content}")
    print(f"Generated {output_path}")
