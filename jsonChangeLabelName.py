import glob
import json
from tqdm import tqdm

label_list = []
file_list = glob.glob('./*.json')
for file in tqdm(file_list):
    # 打开文件取出数据并修改，然后存入变量
    with open(file, 'r') as f:
        data = json.load(f)
        shapes = data['shapes']
        for shape in shapes:
            shape['label'] = shape['label'].replace('sdasd', '')
            if shape['label'] == "RealWhite":
                shape['label'] = "imagWhite"
        if shape['label'] not in label_list:
            label_list.append(shape['label'])
    # 打开文件并覆盖写入修改后内容
    with open(file, 'w') as f:
        json.dump(data, f)

for i in label_list:
    print(i)

